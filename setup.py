import os

from setuptools import setup


NAME = "yandex_speech"
VERSION_PATH = os.path.join(os.path.dirname(__file__), NAME, "VERSION.txt")
with open(VERSION_PATH) as f:
    version = f.read().strip()

setup(
    name=NAME,
    description="A library for Yandex speech kit",
    long_description=open("README.rst").read(),
    url="https://github.com/art1415926535/Yandex_speech",
    version=version,
    packages=[NAME],
    package_data={NAME: ["VERSION.txt"]},
    install_requires=["requests", "six"],
    license="MIT",
    author="Artem Fedotov",
    author_email="art1415926535@ya.ru",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Russian",
        "Natural Language :: English",
        "Natural Language :: Turkish",
        "Natural Language :: Ukranian",
        "Topic :: Multimedia :: Sound/Audio :: Speech"
    ],
    keywords="yandex speech kit text-to-speech tts",
)
