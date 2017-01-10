# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import join, dirname
import yandex_speech_kit


setup(
    name="yandex_speech_kit",
    description="A library for Yandex speech kit",
    long_description=open('README.rst').read(),
    url='https://github.com/art1415926535/Yandex_speech_api',
    version=yandex_speech_kit.__version__,
    packages=find_packages(),
    license='MIT',
    author='Artem Fedotov',
    author_email = "art1415926535@ya.ru",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Russian",
        "Natural Language :: English",
        "Natural Language :: Turkish",
        "Natural Language :: Ukranian",
        "Topic :: Multimedia :: Sound/Audio :: Speech"
    ],
    keywords='yandex speech kit text-to-speech tts',
)
