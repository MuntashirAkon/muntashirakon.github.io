import subprocess
import json
from pathlib import Path
import tempfile
import os
from html.parser import HTMLParser

class CSLRightInlineExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_target = False
        self.depth = 0
        self.chunks = []
        self.results = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "div" and "class" in attrs_dict and "csl-right-inline" in attrs_dict["class"].split():
            self.in_target = True
            self.depth = 1
        elif self.in_target:
            self.chunks.append(self.get_starttag_text())
            self.depth += 1

    def handle_endtag(self, tag):
        if self.in_target:
            if tag == "div" and self.depth == 1:
                # End of the target div
                self.in_target = False
                self.results.append("".join(self.chunks).strip())
                self.chunks = []
                self.depth = 0
            else:
                self.chunks.append(f"</{tag}>")
                self.depth -= 1

    def handle_data(self, data):
        if self.in_target:
            self.chunks.append(data)

    def handle_entityref(self, name):
        if self.in_target:
            self.chunks.append(f"&{name};")

    def handle_charref(self, name):
        if self.in_target:
            self.chunks.append(f"&#{name};")

def bibtex_to_jekyll_html_inner(bibtex_path, csl_path, output_path):
    # Step 1: Convert BibTeX to CSL JSON using pandoc
    csljson = subprocess.run(
        ['pandoc', '-f', 'bibtex', '-t', 'csljson', bibtex_path],
        text=True,
        capture_output=True
    )
    if csljson.returncode != 0:
        raise RuntimeError(f"Pandoc BibTeX conversion failed: {csljson.stderr}")
    entries = json.loads(csljson.stdout)

    # Write full CSL JSON bibliography to a temp file
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as bibfile:
        json.dump(entries, bibfile)
        bibfile.flush()
        bibfile_path = bibfile.name

    results = []
    for entry in entries:
        # Update 'note' entry
        citation_key = entry['id']
        # Create temporary markdown file with citation and References header
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.md', delete=False) as mdfile:
            mdfile.write(f'[@{citation_key}]\n\n# References')
            mdfile.flush()
            mdfile_path = mdfile.name

        # Run Pandoc to generate formatted HTML entry
        formatted = subprocess.run(
            [
                'pandoc',
                mdfile_path,
                '--citeproc',
                f'--csl={csl_path}',
                f'--bibliography={bibfile_path}',
                '-t', 'html'
            ],
            text=True,
            capture_output=True
        )

        os.unlink(mdfile_path)

        if formatted.returncode != 0:
            print(f"⚠️ Skipping {citation_key}: {formatted.stderr}")
            continue

        # Parse HTML output to extract inner HTML of .csl-right-inline
        parser = CSLRightInlineExtractor()
        parser.feed(formatted.stdout)
        inner_html = parser.results[0] if parser.results else ''

        results.append({
            'id': citation_key,
            'html': inner_html,
            'raw': entry
        })

    os.unlink(bibfile_path)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    return results

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: bibtex_to_jekyll.py [BIBTEX_PATH] [CSL_PATH] [OUTPUT_JSON_PATH]")
        sys.exit(1)
    bibtex_path = sys.argv[1]
    csl_path = sys.argv[2]
    output_path = sys.argv[3]
    print(f"📚 Converting {bibtex_path} using {csl_path}...")
    results = bibtex_to_jekyll_html_inner(bibtex_path, csl_path, output_path)
    print(f"✅ Converted {len(results)} entries to {output_path}")
