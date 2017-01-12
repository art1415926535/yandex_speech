import os

import requests


class TTS:
    TTS_URL = "https://tts.voicetech.yandex.net/generate"
    MAX_CHARS = 2000

    def __init__(self, speaker, audio_format, key, lang="ru-RU", **kwargs):
        """Genarator of speech.

        Args:
            speaker: Speaker.
            audio_format: Audio file format.
            key: API‑key for Yandex speech kit.
            lang (optional): Language. Defaults to "ru-RU".
            emotion (optional): The color of the voice. Defaults to "normal".
            speed (optional): Speech tempo. Defaults to 1.0.
        """
        self.__params = {
            "speaker": speaker,
            "format": audio_format,
            "key": key,
            "lang": lang
        }
        self.__params.update(kwargs)
        self._data = None

    def generate(self, text):
        """Try to get the generated file.

        Args:
            text: The text that you want to generate.
        """
        if not text:
            raise Exception("No text to speak")

        if len(text) >= self.MAX_CHARS:
            raise Exception("Number of characters must be less than 2000")

        params = self.__params.copy()
        params["text"] = text
        self._data = requests.get(self.TTS_URL, params=params,
                                  stream=False).iter_content()

    def save(self, path="speech"):
        """Save data in file.

        Args:
            path (optional): A path to save file. Defaults to "speech".
            File extension is optional. Absolute path is allowed.

        Returns:
            The path to the saved file.
        """

        if self._data is None:
            raise Exception("There’s nothing to save")

        extension = "." + self.__params["format"]
        if os.path.splitext(path)[1] != extension:
            path += extension

        with open(path, "wb") as f:
            for d in self._data:
                f.write(d)

        return path
