"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: test-codegen.py

About: Tests for the folllowing files.
    1. core/codegen-lib.py (Smirk implementation library)
    2. core/codegen.py (Smirk runtime script)
"""

from nose.tools import *
from core.codegen_lib import *

def test_HTMLConstruct():
    new_html_node = HTMLConstruct('h1')
    print(new_html_node)
