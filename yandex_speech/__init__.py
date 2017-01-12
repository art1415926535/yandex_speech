import os

from .tts import TTS


VERSION_PATH = os.path.join(os.path.dirname(__file__), "VERSION.txt")
with open(VERSION_PATH) as f:
    __version__ = f.read().strip()
