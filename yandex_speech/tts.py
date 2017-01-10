# -*- coding: utf-8 -*-
import os
import urllib.parse
import requests

def generate_voice(text, extension, speaker, key, lang='ru-RU', path='voice', **kwargs):
    """Generation of speech.

    Args:
        text: Text to speech.
        extension: Audio file format.
        speaker: Speaker.
        key: API‑key.
        lang (optional): Language. Defaults to "ru-RU".
        path (optional): A path to save file. Defaults to "voice".
        emotion (optional): The color of the voice. Defaults to "normal".
        speed (optional): Sspeech tempo. Defaults to 1.0.

    Returns:
        The path to the saved file.
    """

    url = 'https://tts.voicetech.yandex.net/generate?' \
          'text={text}&' \
          'format={extension}&' \
          'speaker={speaker}&' \
          'lang={lang}&' \
          'key={key}&'

    text = urllib.parse.quote(text)

    url = url.format(
        text=text,
        extension=extension,
        lang=lang,
        speaker=speaker,
        key=key
    )

    if kwargs:
        url += urllib.parse.urlencode(kwargs)

    extension = "." + extension
    if os.path.splitext(path)[1] != extension:
        path += extension

    r = requests.get(url, stream=True)

    with open(path, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

    return path
