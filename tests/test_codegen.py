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
    assert(str(new_html_node) == '<h1></h1>')

    # Add an attribute object
    name = HTMLAttributeConstruct('name')
    assert(str(new_html_node.add_attribute(name)))

def test_HTMLAttributeConstruct():
    new_html_attribute = HTMLAttributeConstruct('name')
    print(new_html_attribute)
    assert(str(new_html_attribute) == 'name=""')

def test_HTMLInnerTextConstruct():
    new_html_inner_text = HTMLInnerTextConstruct('hello world')
    print(new_html_inner_text)
    assert(str(new_html_inner_text.content_str) == 'hello world')

def test_FileNameConstruct():
    new_filename = FileNameConstruct('test', file_extensions['html'])
    print(new_filename)

    new_filename.prepend('previousdir')
    assert(new_filename.name == new_filename.filename_str + new_filename.extension_str)
    