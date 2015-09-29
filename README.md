<h2>Генерация речи средствами <a href="https://tech.yandex.ru/speechkit/">Yandex SpeechKit</a></h2>

<h4>Функция generate_voice</h4>
  <b>Параметры:</b>
  
    file=<название файла для сохранения> - по умолчанию "voice.mp3"
    text=<текст для генерации> - "гот%2bов"
    format=<формат аудио файла> - "mp3", "wav"
    lang=<язык> - "ru‑RU"
    speaker=<голос> - female: jane, omazh; male: zahar, ermil
    key=<API‑ключ>
    
    [emotion=<окраска голоса>] - neutral(нейтральный), evil (злой), mixed (переменная окраска)
    [drunk=<окраска голоса>] - true, false
    [ill=<окраска голоса>] - true, false
    [robot=<окраска голоса>] - true, false
    
  <b>Возвращает</b> название файла с сохранённым синтезированным голосом
