import os

from .tts import TTS


with open(os.path.join("yandex_speech", "VERSION.txt")) as f:
    __version__ = f.read().strip()
