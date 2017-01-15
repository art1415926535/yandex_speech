============================
yandex_speech
============================

Generation of speech using `Yandex SpeechKit <https://tech.yandex.ru/speechkit/>`_.
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
`Text to speech <https://github.com/art1415926535/yandex_speech#text-to-speech>`_

Speech to text (not ready)

`Natural language understanding <https://github.com/art1415926535/yandex_speech#natural-language-understanding>`_

****

Text to speech
--------------
.. code-block:: python

    >>> from yandex_speech import TTS
    >>> tts = TTS("jane", "mp3", "60589d42-0e42-b742-8942-thekeyisalie")
    >>> tts.generate("Привет мир")
    >>> tss.save()
    speech.mp3

TTS(speaker, audio_format, key, lang="ru‑RU", emotion="neutral", speed=1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- ``speaker`` - Speaker. Female: "jane", "oksana", "alyss", "omazh". Male: "zahar", "ermil";
- ``audio_format`` - Audio file format: "mp3", "wav", "opus";
- ``key`` - `API‑key for Yandex speech kit <https://developer.tech.yandex.ru>`_.
- ``lang`` (optional) - Language: "ru‑RU" (by default), "en-US", "tr-TR", "uk-UK";
- ``emotion`` (optional) - The color of the voice: "neutral" (by default), "evil", "good";
- ``speed`` (optional) - Speech tempo: a value between 0.1 (slowest) to 3.0 (fastest).


tts.generate(text)
~~~~~~~~~~~~~~~~~~
- ``text`` - Text to speech: "з+амок" (before the stressed vowel can be put "+"; the restriction on line length: 2000 bytes);

tts.save(path="speech")
~~~~~~~~~~~~~~~~~~~~~~~
- ``path`` (optional) - A path to save file: "test", "dirname/test.mp3", ...;
Returns the path.

References
----------
`Overview tts technology
<https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-overview-technology-tts-docpage/>`_

`The format of request and response
<https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-tts-docpage/>`_

****

Natural language understanding
------------------------------
.. code-block:: python

    >>> from yandex_speech import NLU
    >>> nlu = NLU("60589d42-0e42-b742-8942-thekeyisalie")
    >>> nlu.parse("31 апреля родился Хлусов Геннадий Викторович", ("Date", "Fio"))
    {'Date': [{'Tokens': {'Begin': 0, 'End': 2}, 'Month': 4, 'Day': 31}], 'Fio': [{'Patronymic': 'викторович', 'Type': 'fioname', 'Tokens': {'Begin': 3, 'End': 6}, 'FirstName': 'генадий', 'LastName': 'хлусов'}]}

NLU(key)
~~~~~~~~
- ``key`` - `API‑key for Yandex speech kit <https://developer.tech.yandex.ru>`_.

NLU.parse(text, layers=None)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- ``text`` - Text to parse.
- ``layers`` (optional) - Special fields. Only one string or iterable object (e.g "Data", ("Data", "Fio")). Only these fields will be returned.

Returns the parsed text into a json object.

References
----------

`Overview nlu technology
<https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-overview-technology-nlu-docpage/>`_

The format of `request <https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-nlu-params-docpage/>`_ and `response <https://tech.yandex.ru/speechkit/cloud/doc/dg/concepts/speechkit-dg-nlu-response-docpage/>`_
