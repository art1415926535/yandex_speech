import urllib.request
import urllib.parse
import urllib


def generate_voice(text, extension, speaker, key, filename='voice', **kwargs):
    """
    text=<текст для генерации> - "гот%2bов"
    extension=<формат аудио файла> - "mp3", "wav", "opus"
    lang=<язык> - "ru‑RU"
    speaker=<голос> - female: jane, omazh; male: zahar, ermil
    key=<API‑ключ>

    [emotion=<окраска голоса>] - neutral(нейтральный), evil (злой), mixed (переменная окраска)
    [drunk=<окраска голоса>] - true, false
    [ill=<окраска голоса>] - true, false
    [robot=<окраска голоса>] - true, false
    """

    url = 'https://tts.voicetech.yandex.net/generate?' \
          'text={text}&' \
          'format={audio_format}&' \
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

    filename += '.' + extension
    urllib.request.urlretrieve(url, filename)
    return filename
