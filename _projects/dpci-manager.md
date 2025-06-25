---
layout: project
title: "Project: DPCI Manager"
name: DPCI Manager
description: "A utility software for macOS to visualise PCI hardware information and a produce output similar to Linux's lspci."
priority: 15
selected: true
link: https://github.com/MuntashirAkon/DPCIManager
---

[DPCI Manager](https://github.com/MuntashirAkon/DPCIManager) was a popular utility software in the [Hackintosh](https://en.wikipedia.org/wiki/Hackintosh) community which is now succeeded by [Hackintool](https://github.com/benbaker76/Hackintool). It primarily displays the [PCI](https://en.wikipedia.org/wiki/Peripheral_Component_Interconnect) hardware information fetched from the operating system which are not necessarily the same as the original hardware information since many of them are emulated by editing the [ACPI](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface) tables. It also offers a dedicated section to display audio, network and graphics information since configuring these options in a Hackintosh is quite difficult. A tool, namely `dspci`, is also developed as part of the project which produces outputs identical to the Linux command `lspci`. The software was downloaded at least thirty-six thousand times.
<div class="flex center middle">
  <div class="layout-1-2">
    <img style="max-width: 40rem; margin: 0 1rem" src="{{ '/images/dpci-manager-main.png' | relative_url }}" alt="DPCI Manager: main UI">
  </div>
  <div class="layout-1-2">
    <img style="max-width: 40rem; margin: 0 1rem" src="{{ '/images/dpci-manager-pci.png' | relative_url }}" alt="DPCI Manager: PCI list page">
  </div>
</div>
