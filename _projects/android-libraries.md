---
layout: project
title: "Project: Android Libraries"
name: Android Libraries
description: "Android Libraries aims at building a database of frequently used Android libraries containing primary signatures (eg. Java package name), licenses, anti-features, etc."
priority: 6
link: https://github.com/MuntashirAkon/android-libraries
---

<div class="flex">
  <div class="layout-2-3" markdown="block">
[Android Libraries](https://github.com/MuntashirAkon/android-libraries) aims at building a database of frequently used Android libraries containing primary signatures (eg. Java package name), licenses, [anti-features](https://f-droid.org/docs/Anti-Features/), etc. These data can be used to gather insights on libraries used by an *unobfuscated* Android application, and a user can decide whether to install the application based on their threat model. This is one of the first open source projects to systematically list such signatures. The list is based on the works of [IzzyOnDroid](https://gitlab.com/IzzyOnDroid/repo/-/tree/master/lib) and [Exodus](https://exodus-privacy.eu.org/) in addition to signatures investigated by the [App Manager](https://github.com/MuntashirAkon/AppManager) contributors. This project is currently in progress and only being used by App Manager. Once it is stable, third-party apps will be able to use the list to display insights to the users.
  </div>
  <div class="layout-1-3 center">
    <figure style="display: block">
      <img style="max-width: 24rem; margin: 0 1rem" src="{{ '/images/androlibs-am.png' | relative_url }}" alt="Described in the caption">
      <figcaption>Screenshot from <a href="https://github.com/MuntashirAkon/AppManager">App Manager</a> displaying a list of trackers and libraries in an app taken from the project.</figcaption>
    </figure>
  </div>
</div>
