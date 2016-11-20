"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: test_smirk_lang.py

About: Tests for the following files.
    1. core/smirk_lang.py (Smirk implementation library)
    2. core/smirk_lang_parse.py (Smirk runtime script)
"""

print('........runnning core/test_smirk_lang.py')

from nose.tools import *
from core.smirk_lang import *
from core.smirk_lang_parse import *

def test_SmirkTag():
    tagblock = SmirkTag()
    assert(tagblock.__str__() == '<smirk></smirk>')
    