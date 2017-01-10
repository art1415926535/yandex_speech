# -*- coding: utf-8 -*-
import os
import urllib.request
import urllib.parse
import urllib


def generate_voice(text, extension, speaker, key, path='voice', **kwargs):
    """Generation of speech.

    Args:
        text: Text to speech.
        extension: Audio file format.
        lang: Language.
        speaker: Speaker.
        key: API‑key.
        path (optional): A path to save file. Defaults to "voice".
        emotion (optional): The color of the voice. Defaults to "normal"
        speed (optional): Sspeech tempo. Defaults to 1.0

    Returns:
        The path to the saved file.
    """

    url = 'https://tts.voicetech.yandex.net/generate?' \
          'text={text}&' \
          'format={extension}&' \
          'lang=ru-RU&' \
          'speaker={speaker}&' \
          'key={key}&'

    text = urllib.parse.quote(text)

    url = url.format(
        text=text,
        audio_format=audio_format,
        speaker=speaker,
        key=key
    )

    if kwargs:
        url += urllib.parse.urlencode(kwargs)

    if os.path.splitext(path)[1] != extension:
        path += '.' + extension

    urllib.request.urlretrieve(url, path)

    return path
