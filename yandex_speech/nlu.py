import collections

import requests
import six


class NLU:
    NLU_URL = "https://vins-markup.voicetech.yandex.net/markup/0.x/"

    def __init__(self, key):
        """Class for parse input text.

        Args:
            key: API-key for Yandex speech kit.
        """
        self.key = key

        self.__test_the_key()

    def __test_the_key(self):
        """Test the validity of the key.
        """
        params = {
            "text": "test",
            "key": self.key,
        }

        status = requests.get(self.NLU_URL, params=params).status_code
        if status == 400:
            raise Exception("Key banned or inactive")

    def parse(self, text, layers=None):
        """Parsing passed text to json.

        Args:
            text: Text to parse.
            layers (optional): Special fields. Only one string
                or iterable object (e.g "Data", ("Data", "Fio")).
                Only these fields will be returned.


        Returns:
            The parsed text into a json object.
        """
        params = {
            "text": text,
            "key": self.key,
        }

        if layers is not None:
            # if it's string
            if isinstance(layers, six.string_types):
                params["layers"] = layers

            # if it's another iterable object
            elif isinstance(layers, collections.Iterable):
                params["layers"] = ",".join(layers)

        req = requests.get(self.NLU_URL, params=params)
        return req.json()
