# Staticademia

A template for static website built using Jekyll.

## Requirements

These are the basic requirements:
- Jekyll
- Bundler: `gem install bundler` (optional)

These dependencies are required for converting `.bib` files
- Python3
- Pandoc

## Building

In general, GitHub is able to build and serve the static website. For testing, at first you need to install all the dependencies using `bundle`:

```sh
bundle install --path vendor/bundle
```

Or, if you prefer without `bundle`:

```sh
gem install github-pages
```

After that you can run a development server locally:

```sh
jekyll serve --livereload
```

You may need to prefix execute `jekyll` commands with `bundle exec` if you're using Bundler.

## Deployment

Follow the usual procedure. For GitHub, the usual procedure involves creating a repository called `<username>.github.io` and configuring the path in the repository settings. For other hosting providers, you may need to build it manually:

```sh
jekyll build
```

Then, you need to upload the contents of the folder `_site` to the root directory of your hosting provider `public_html` or a similar directory.

If the path is a subdirectory (e.g., `example.com/mysite` instead of `example.com`), you also need to add the following items in the `_config.yml` file:

```yml
url: example.com # Optional
baseurl: /mysite # Compulsory
```

## Getting Started

In general, you only need to edit the contents of the following folders depending on your need:

- `_data`: Contains all the necessary data to generate a proper static site
- `_education`: Contains education related info
- `_employment`
- `_gallery`
- `_projects`
- `_scripts`: Contains utility scripts
- `_teaching`
- `css`: Contains CSS files
- `fonts`
- `images`
- `js`
- `pdfs`
- `_includes/intro.md`: The introduction in the homepage should go here (instead of adding them directly to the `index.md` file).

Also, if you're not familiar with Markdown format, not that anything between `---` at the top of a file represents the frontmatter of the file, and they are written in YAML format.

### Generating favicons
For a proper website, favicons are absolutely necessary. Icons can be either the university monogram or your self-potrait. You can utilize <https://favicon.io> to generate necessary images. After downloading the images, make sure to place them properly.
`favicon.ico` must be located at the root directory, the rests go to the `images` directory.

### Updating configurations
Necessary configurations can be updated by modifying `_config.yml`. In general, you need to update the title, logo, author, description, academic info, social media info, and select which pages to display. You can also control which features should be enabled for your homepage. By default, everything is enabled. To disable a social media profile, simply leave it empty, and to disable any pages or feature, set it to `false`.

### Updating other information
Some other information can be updated using the files in the `_data` folder. Here are the complete list of files in the folder and their description:
- `acm.csl`: A CSL file that formats the bibliography. In general, you do not need to edit this file. Note that it does not strictly follow the ACM citation standard.
- `awards.csv`: It should contain the awards and honors you have received over the years in descending order. The first entry is year and the second is the description. It supports both Markdown and HTML syntax, but make sure to use double quotation if you use any commas since entries in each line are separated by comma.
- `conferences.bib`: The conference papers that you have published in Bibtex format.
- `conferences.json`: This is a generated file (see below), please DO NOT EDIT.
- `journals.bib`: The journal papers that you have published in Bibtex format.
- `journals.json`: This is a generated file (see below), please DO NOT EDIT.
- `names.yml`: The names you have used over the years with your publications. They will be automatically highlighted during the site generation. Each line contains a single entry followed by a `- ` (YAML format).
- `news.csv`: Similar to `awards.csv`, but it contains the recent news. By default, only top three items are displayed in the homepage, the rests are collapsed.

### Converting `.bib` files into Jekyll-readable JSON files

Jekyll cannot directly read `.bib` files. So, you need to convert it to Jekyll-readable JSON files. To convert both journals and conferences at once, you can run the following commands in the root directory:

```sh
python _scripts/bibtomd.py _data/conferences.bib _data/acm.csl _data/conferences.json
python _scripts/bibtomd.py _data/journals.bib _data/acm.csl _data/journals.json
```

### Additional formatting for `.bib` files
In addition to the regular Bibtex format, some unused fields have been remapped for specific usage.
- `note`: include a link to the PDF version of the paper (e.g., `note={pdfs/paper.pdf}`). If this field is set, `[PDF]` will be appened to the bibliography item with a hyperlink that points to the PDF.
- `annote`: use this field to add any potential awards (e.g., `annote={Best Paper Award}`). This contents of this particular field will be highlighted in purple with a ★ (star) prefix.
- `version`: use this field to highlight the venue (e.g., `version={S&P'21}`). The highlighted venue will be prepended to the bibliography item.


### Adding/updating projects

Projects go to the `_projects` directory. Each entry in the projects directory represents a project. They should either have an `.md` or `.html` extension.

The frontmatter should contain the following items:

```yml
layout: project
title: "Project: Project name"
name: "Project name"
description: "Project description"
priority: 3 # lower the number => higher the priority => goes on top of the list
link: https://example.com
```

If you want to highlight the project in the homepage, make sure to include `selected: true` as well. After the frontmatter, you can add extended description for the project, screenshots, etc.

### Adding/updating teaching

Teaching documentation goes to the `_teaching` directory. Each entry in this directory represents a separate teaching job. They should either have an `.md` or `.html` extension. THe frontmatter should contain the following items:

```yml
layout: teaching
title: Teaching at University Name
institute: University Name
country: Country Name
position: Position in the university (e.g., Lecturer)
duration: Either session/quarter/semester or a date range (e.g., Spring 2025 &mdash; Summer 2025)
date: 2025-04-01 # Date started, this is used for sorting
courses:
  - code: Course code (e.g., CS 256)
    title: Course title (e.g., Computer Security)
    sessions: Sessions taught, you can also include links to those session (e.g., <a href=\"https://example.com\">Spring 2025</a>)
```

Additional description can be added after the frontmatter, but they are generally not required.

### Adding/updating employment

Employment information goes to the `_employment` directory. Each entry in this directory represents a separate job. They should either have an `.md` or `.html` extension. THe frontmatter should contain the following items:

```yml
layout: employment
title: My Position at This Company
company: This Company
country: Country Name
position: My Position
type: Remote # Job type, optional
duration: Date range (e.g., January 2021 &mdash; September 2022)
date: 2025-04-01 # Date started, this is used for sorting
```

Additional description can be added after the frontmatter.

### Adding/updating education

Education information goes to the `_education` directory. Each entry in this directory represents a separate degree. They should either have an `.md` or `.html` extension. THe frontmatter should contain the following items:

```yml
layout: education
title: My Degree at This University
institute: This University
country: Country Name
degree: My Degree in This Subject
degree_short: M.D. in TS
duration: Date range (e.g., September 2024 &mdash; present)
date: 2024-09-25 # Date started or finished, this is used for sorting
extras: # Optional
  - key: Key (e.g., Adviser) # Optional
    value: Value (e.g., Dr. Victor Frankenstein) # Compulsory
```

Additional description can be added after the frontmatter.

### Adding/updating gallery

Image gallery goes to the `_gallery` directory. Each entry in this directory represents a separate album. They should either have an `.md` or `.html` extension. THe frontmatter should contain the following items:

```yml
layout: gallery
title: Album Title
priority: 1 # lower the number => higher the priority => goes on top of the list
gallery:
  - src: path/to/image (e.g., images/image_1.jpg) # Compulsory
    cap: Caption for the image # Optional
    cpy: Short copyright statement (e.g., Someone/CC-BY-SA-4.0) # Optional
```

Additional description can be added after the frontmatter.
