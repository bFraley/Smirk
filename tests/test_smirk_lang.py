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

def test_SmirkTemplateTag():
    tagblock = SmirkTemplateTag()
    assert(tagblock.__str__() == '<smirk></smirk>')

def test_SmirkControlToken():
    pass

def test_SmirkComparisonToken():
    pass

def test_SmirkExtensionToken():
    pass
    
def test_SmirkCoreErrorToken():
    pass

def test_SmirkDefineErrorToken():
    pass

def test_SmirkCoreLib():
    lib = SmirkCoreLib();
    assert(lib.add(1, 2) == 3)
    assert(lib.sub(1, 2) == -1)
    assert(lib.mult(2, 4) == 8)
    assert(lib.div(2, 1) == 2)
    assert(lib.mod(19, 2) == 1)
    assert(lib.instring('hello', 'testhello') == True)
    assert(lib.cat('he', ('llo' + ' test')) == 'hello test')
    assert(lib.are_exact_names('test', 'test') == True)
    assert(lib.are_exact_values(1, '1') == False)
    