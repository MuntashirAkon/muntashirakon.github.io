---
layout: default
title: Projects
---

{% assign sorted_projects = site.projects | sort: 'priority' %}
{% for project in sorted_projects %}
## {{ project.name }}
{{ project.content }}
{% endfor %}

### Other projects
I've also created and/or developed a number of open source projects, such as [PHPPhylogeneticTrees](https://github.com/MuntashirAkon/PHPPhylogeneticTrees), [PHPPListEditor](https://github.com/MuntashirAkon/PHPPListEditor), [RNGTests](https://github.com/MuntashirAkon/RNGTests), [Chrome OS Multiboot](https://github.com/MuntashirAkon/Chrome-OS-Multiboot), [Chrome OS Updater](https://github.com/MuntashirAkon/chrome_os_updater), [apksig for Android](https://github.com/MuntashirAkon/apksig-android), [Magic MIME DB](https://github.com/MuntashirAkon/magic-mime-db) (work in progress), [CountdownTimer](https://github.com/MuntashirAkon/CountdownTimer), [AppleIntelFramebufferPlatformInfo](https://github.com/MuntashirAkon/AppleIntelFramebufferPlatformInfo), etc.

I have contributed to a number of projects, such as [IINA](https://github.com/iina/iina), [MaciASL-patchmatic](https://github.com/RehabMan/OS-X-MaciASL-patchmatic), [maclog](https://github.com/syscl/maclog), [pycookiecheat](https://github.com/n8henrie/pycookiecheat), [Intent Intercept](https://github.com/MuntashirAkon/intent-intercept), [Autostarts](https://github.com/miracle2k/android-autostarts), [Robolectric](https://github.com/robolectric/robolectric), [Material Components Android](https://github.com/material-components/material-components-android), [Sora Editor](https://github.com/Rosemoe/sora-editor), [ARSCLib](https://github.com/REAndroid/ARSCLib), etc.