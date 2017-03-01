# -*- coding: utf-8 -*-
import unittest

from yandex_speech import NLU


KEY = "secret"

TEXTS = {
    "Date": "7 июля 2007 года",
    "Fio": "иванов иван иванович",
}


class TestInit(unittest.TestCase):
    """Test initialization and an incorrect key."""

    def test_init(self):
        self.assertIsNotNone(NLU(KEY))

        with self.assertRaises(Exception):
            NLU("chimichanga")


class TestRequest(unittest.TestCase):
    """Testing the queries, layers and data."""

    def setUp(self):
        self.nlu = NLU(KEY)

    def test_only_text(self):
        self.assertIsNotNone(self.nlu.parse(TEXTS["Date"]))

    def test_text_and_layers(self):
        some_json = self.nlu.parse(TEXTS["Date"], "Date")
        self.assertIsNotNone(some_json)

        same_json = self.nlu.parse(TEXTS["Date"], ("Date",))
        self.assertEqual(some_json, same_json)

        self.nlu.parse(
            " ".join(TEXTS.values()),
            layers=list(TEXTS.keys())
        )
