============================
yandex_speech
============================

Generation of speech using `Yandex SpeechKit
<https://tech.yandex.ru/speechkit/>`_.
SpeechKit Cloud allows you to voice any text in Russian or English.
You can choose the voice (male or female), tempo and intonation (e.g., joy).

.. image:: https://img.shields.io/pypi/v/yandex_speech.svg
    :target: https://pypi.python.org/pypi/yandex_speech

.. image:: https://img.shields.io/travis/art1415926535/yandex_speech.svg
    :target: https://travis-ci.org/art1415926535/yandex_speech

.. image:: https://landscape.io/github/art1415926535/Yandex_speech/master/landscape.svg?style=flat
    :target: https://landscape.io/github/art1415926535/Yandex_speech/master

Installation
------------
Use ``Pip``, Luke

.. code-block:: bash

    $ pip install yandex_speech

Usage
-----
.. code-block:: python

    from yandex_speech import TTS
    tts = TTS("jane", "mp3", "60589d42-0e42-b742-8942-thekeyisalie")
    tts.generate("Привет мир")
    tss.save()

TTS(speaker, audio_format, key, lang="ru‑RU", emotion="neutral", speed=1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Required parameters:*

- ``speaker`` - Speaker. Female: "jane", "oksana", "alyss", "omazh". Male: "zahar", "ermil";
- ``audio_format`` - Audio file format: "mp3", "wav", "opus";
- ``key`` - `API‑key for Yandex speech kit<https://developer.tech.yandex.ru>`_.

*Optional parameters:*

- ``lang`` - Language: "ru‑RU" (by default), "en-US", "tr-TR", "uk-UK";
- ``emotion`` - The color of the voice: "neutral" (by default), "evil", "good";
- ``speed`` - Speech tempo: a value between 0.1 (slowest) to 3.0 (fastest).


tts.generate(text)
~~~~~~~~~~~~~~~~~~~~~~~
- ``text`` - Text to speech: "з+амок" (before the stressed vowel can be put "+"; the restriction on line length: 2000 bytes);

tts.save(path="speech")
~~~~~~~~~~~~~~~~~~~~~~~
- ``path`` (optional) - A path to save file: "test", "dirname/test.mp3", ...;
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
