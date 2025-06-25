---
layout: project
title: "Project: LibADB Android"
name: LibADB Android
description: "An Android library to let applications utilise <a href=\"https://en.wikipedia.org/wiki/Android_Debug_Bridge\" target=\"_blank\" rel=\"noreferrer\">Android Debug Bridge</a> (ADB) to perform operations that may require more privileges than that is offered by Android for third-party applications."
priority: 5
selected: true
link: https://github.com/MuntashirAkon/libadb-android
---

[LibADB Android](https://github.com/MuntashirAkon/libadb-android) is an Android library to let applications utilise [Android Debug Bridge](https://en.wikipedia.org/wiki/Android_Debug_Bridge) (ADB) to perform operations that may require more privileges than that is offered by Android for third-party applications. This is the only known library that offers connections through [wireless debugging](https://developer.android.com/tools/adb#connect-to-a-device-over-wi-fi). The primary challenge was getting rid of the [BoringSSL](https://github.com/google/boringssl) dependency which has [an ugly license](https://github.com/google/boringssl/blob/master/LICENSE) that makes it incompatible with the most open source licenses including GNU Public License (GPL). It was replaced with a custom [SPAKE2](https://www.ietf.org/id/draft-irtf-cfrg-spake2-26.html) implementation written in [Java](https://github.com/MuntashirAkon/spake2-java) and [C](https://github.com/MuntashirAkon/spake2-c).
