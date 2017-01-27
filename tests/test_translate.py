# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mtranslate import translate
import unittest
import re

from nose.tools import *  # PEP8 asserts
from nose.plugins.attrib import attr


from mtranslate import translate

@attr("requires_internet")
class TestTranslatorIntegration(unittest.TestCase):

    """Integration tests that actually call the translation API."""

    def setUp(self):
        self.sentence = 'Selamat datang di Indonesia'


    def test_translate(self):
        to_en = translate(self.sentence, to_language="en", from_language="id")
        assert_equal(to_en, "Welcome to Indonesia")

    def test_translate_missing_from_language_auto_detects(self):
        translated = translate(self.sentence, to_language="en")
        assert_equal(translated, "Welcome to Indonesia")


if __name__ == '__main__':
    unittest.main()
