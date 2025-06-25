---
layout: project
title: "Project: Captive Portal Controller"
name: Captive Portal Controller
description: "A utility software for Android to primarily address <a href=\"https://mullvad.net/en/blog/2022/10/10/android-leaks-connectivity-check-traffic/\" target=\"_blank\" rel=\"noreferrer\">the connectivity leaks</a> related to <a href=\"https://en.wikipedia.org/wiki/Captive_portal\" target=\"_blank\" rel=\"noreferrer\">captive portals</a> and connectivity checks when VPN is enabled."
priority: 2
selected: true
link: https://github.com/MuntashirAkon/CaptivePortalController
---

<div class="flex">
  <div class="layout-2-3" markdown="block">
[Captive Portal Controller](https://github.com/MuntashirAkon/CaptivePortalController) is a utility software for Android to primarily address [the connectivity leaks](https://mullvad.net/en/blog/2022/10/10/android-leaks-connectivity-check-traffic/) which reveals the real IP address when VPN is enabled. The leaks affect [captive portals](https://en.wikipedia.org/wiki/Captive_portal) (often necessary when logging into a public network) and Internet connectivity checks which is [almost always done through Google's servers](https://grapheneos.org/faq#default-connections), which is a breach of privacy. However, the app can also be used to avoid other captive portal-related attacks usually done by setting up a malicious captive portal in a Wi-Fi network obtained through other typical Wi-Fi attacks. For connectivity checks, the app can either disable it entirely or keep it enabled using a more privacy-friendly alternative such as [GrapheneOS](https://grapheneos.org/faq#default-connections) or [Kuketz](https://www.kuketz-blog.de/empfehlungsecke/#captive-portal). It also allows you to set a custom [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent) for default connections in Android in case the OEM altered it to something else in order to track the user through, say, connectivity checks.
  </div>
  <div class="layout-1-3 center">
    <img style="max-width: 24rem; margin: 0 1rem" src="{{ '/images/cpc.png' | relative_url }}" alt="Captive Portal Controller UI">
  </div>
</div>