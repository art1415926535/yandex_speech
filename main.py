import os
import urllib.request
import urllib.parse
import urllib


def generate_voice(text, extension, speaker, key, path='voice', **kwargs):
    """
    text=<текст для генерации> - "з+амок" (перед ударной гласной можно ставить "+"; ограничение на длину строки: 2000 байт)
    extension=<формат аудио файла> - "mp3", "wav", "opus"
    lang=<язык> - "ru‑RU", "en-US", "tr-TR", "uk-UK"
    speaker=<голос> - female: jane, oksana, alyss, omazh; male: zahar, ermil
    key=<API‑ключ>

    [emotion=<окраска голоса>] - neutral (нейтральный; используется по умолчанию), evil (раздраженный), good (радостный, доброжелательный)
    [speed=<скорость речи>] - значение от 0,1 (самый медленный темп) до 3,0 (самый быстрый темп).
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
