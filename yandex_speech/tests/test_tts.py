# -*- coding: utf-8 -*-
import os
import random

from shutil import rmtree
import unittest

from yandex_speech.tts import TTS


TEXT = "Привет Яндекс"
SPEAKERS = ("jane", "oksana", "alyss", "omazh", "zahar", "ermil")
AUDIO_FORMATS = ("mp3", "wav", "opus")
LANGUAGES = ("ru‑RU", "en-US", "tr-TR", "uk-UK")
EMOTIONS = ("neutral", "evil", "good")
SPEEDS = (0.1, 1.0, 3.0)

# please don"t use in their projects
KEY = "secret"


class TestInit(unittest.TestCase):
    """Test TTS init"""

    def test_init(self):
        tts = TTS(SPEAKERS[0], AUDIO_FORMATS[0], KEY)

        self.assertEqual(tts._TTS__params["speaker"], SPEAKERS[0])
        self.assertEqual(tts._TTS__params["format"], AUDIO_FORMATS[0])
        self.assertEqual(tts._TTS__params["key"], KEY)
        self.assertEqual(tts._TTS__params["lang"], "ru-RU")

    def test_init_with_kwargs(self):
        speed = random.choice(SPEEDS)
        lang = random.choice(LANGUAGES)
        emotion = random.choice(EMOTIONS)

        tts = TTS(SPEAKERS[0], AUDIO_FORMATS[0], KEY,
                  speed=speed, lang=lang, emotion=emotion)

        self.assertEqual(tts._TTS__params["speaker"], SPEAKERS[0])
        self.assertEqual(tts._TTS__params["format"], AUDIO_FORMATS[0])
        self.assertEqual(tts._TTS__params["key"], KEY)
        self.assertEqual(tts._TTS__params["lang"], lang)
        self.assertEqual(tts._TTS__params["speed"], speed)
        self.assertEqual(tts._TTS__params["emotion"], emotion)


class TestGenerate(unittest.TestCase):
    """Test tts"""

    def setUp(self):
        self.tts = TTS(SPEAKERS[0], AUDIO_FORMATS[0], KEY)

    def test_wrong_text(self):
        # empry string
        self.assertRaises(Exception, self.tts.generate, "")

        # a lot of chars
        self.assertRaises(Exception, self.tts.generate,
                          "a" * self.tts.MAX_CHARS)

    def test_data(self):
        self.tts.generate(TEXT)

        # data received
        self.assertIsNotNone(self.tts._data)

        # more words than more data
        self.other_tts = TTS(SPEAKERS[0], AUDIO_FORMATS[0], KEY)
        self.other_tts.generate(TEXT * 2)
        self.assertLess(list(self.tts._data), list(self.other_tts._data))


class TestSave(unittest.TestCase):
    """Test save files"""

    def setUp(self):
        self.tts = TTS(SPEAKERS[0], AUDIO_FORMATS[0], KEY)
        self.tts.generate(TEXT)

        # create temp dir for tests
        self.tmp_dir = "tmp"
        os.makedirs(self.tmp_dir)
        os.chdir(self.tmp_dir)

    def test_save(self):
        path = self.tts.save()
        self.assertTrue(os.path.isfile(path))

    def test_save_as(self):
        filename = "wonderful_speech"

        path = self.tts.save(filename)
        self.assertTrue(os.path.isfile(path))

        path = self.tts.save(filename + "." + AUDIO_FORMATS[0])
        self.assertTrue(os.path.isfile(path))

        # save to another dir
        another_dir = "amazing_directory"
        os.makedirs(another_dir)
        path = self.tts.save(os.path.join(another_dir, filename))
        self.assertTrue(os.path.isfile(path))

    def tearDown(self):
        # exit and remove temp dir
        os.chdir("..")
        rmtree(self.tmp_dir, ignore_errors=True)


class TestSaveWithoutData(unittest.TestCase):
    """ Specific test """

    def test_save_without_data(self):
        tmp_dir = "tmp"
        os.makedirs(tmp_dir)
        os.chdir(tmp_dir)

        tts = TTS(SPEAKERS[0], AUDIO_FORMATS[0], KEY)
        # save without call generate
        self.assertRaises(Exception, tts.save, "empty_data")
        self.assertFalse(os.path.isfile("empty_data"))

        os.chdir("..")
        rmtree(tmp_dir, ignore_errors=True)
