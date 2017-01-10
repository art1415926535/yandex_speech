============================
Yandex speech kit for Python
============================

Generation of speech using `Yandex SpeechKit
<https://tech.yandex.ru/speechkit/>`_.

1. Import module
    ``from yandex_speech import tts``

2. Call a function
    ``tts.generate_voice("Привет", "mp3", "jane", "60589d42-0e42-b742-8942-thekeyisalie")``

    *Required parameters:*

    - ``text`` - Text to speech: "з+амок" (before the stressed vowel can be put "+"; the restriction on line length: 2000 bytes);
    - ``extension`` - Audio file format: "mp3", "wav", "opus";
    - ``speaker`` - Speaker
        - female: "jane", "oksana", "alyss", "omazh";
        - male: "zahar", "ermil";
    - ``key`` - `API‑key <https://developer.tech.yandex.ru>`_.

    *Optional parameters:*

    - ``lang`` - Language: "ru‑RU", "en-US", "tr-TR", "uk-UK";
    - ``path`` - A path to save file: "test", "dirname/test", "test.mp3", "dirname/test.mp3";
    - ``emotion`` - The color of the voice: "neutral" (by default), "evil", "good";
    - ``speed`` - Speech tempo: a value between 0.1 (slowest) to 3.0 (fastest).

    Returns the path.

References
----------
`SpeechKit Cloud API
<https://tech.yandex.ru/speechkit/cloud/doc/intro/overview/concepts/about-docpage/>`_

`Overview technology
<https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-overview-technology-tts-docpage/>`_

`The format of request and response
<https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-tts-docpage/>`_

`SpeechKit Key
<https://developer.tech.yandex.ru>`_
