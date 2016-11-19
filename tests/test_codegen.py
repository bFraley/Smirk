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

# HTML Constructs Tests
# ---------------------

def test_HTMLConstruct():
    new_html_node = HTMLConstruct('h1')
    print(new_html_node)
    assert(str(new_html_node == '<h1></h1>'))

    # Add an attribute object
    name = HTMLAttributeConstruct('name')
    assert(str(new_html_node.add_attribute(name)))

def test_HTMLAttributeConstruct():
    new_html_attribute = HTMLAttributeConstruct('name')
    print(new_html_attribute.result)
    assert(new_html_attribute.result == 'name=""')

def test_HTMLInnerTextConstruct():
    new_html_inner_text = HTMLInnerTextConstruct('hello world')
    print(new_html_inner_text)
    assert(str(new_html_inner_text.content_str) == 'hello world')


# Test Script Combining HTML Constructs Codegen
# ---------------------------------------------

def test_HTMLCodeGen():

    # Test HTMLConstruct
    # Setup wrapper parent element, init class and id attributes
    wrapper_div = HTMLConstruct('div')

    # Test HTMLAttributeConstruct
    class_attr = HTMLAttributeConstruct('class', 'my-class')
    id_attr = HTMLAttributeConstruct('id', 'my-id')

    # Test HTMLConstruct.add_attribute
    wrapper_div.add_attribute(class_attr)
    wrapper_div.add_attribute(id_attr)
    assert(len(wrapper_div.test_attributes) > 0)

    # Test HTMLInnerTextConstruct
    wrapper_text = HTMLInnerTextConstruct("Hello from parent element!")
    
    # Test HTMLConstruct.add_innertext
    wrapper_div.add_innertext(wrapper_text)

    # HTMLConstruct more elements for child_node tests
    # 2 Paragraphs (direct children)
    par1 = HTMLConstruct('p')
    par2 = HTMLConstruct('p')

    # Create inner text values for par1, and par2
    par1_text = HTMLInnerTextConstruct('Paragraph 1')
    par2_text = HTMLInnerTextConstruct('Paragraph 2')

    # Add inner text for par1 and par 2
    par1.add_innertext(par1_text)
    par2.add_innertext(par2_text)
    
    # Test HTMLConstruct.add_child_element
    wrapper_div.add_child_element(par1)
    wrapper_div.add_child_element(par2)

    print(wrapper_div.get_full_element_result())

# File Name Constructs Tests
# --------------------------

def test_FileNameConstruct():
    new_filename = FileNameConstruct('test', file_extensions['html'])
    print(new_filename)

    new_filename.prepend('previousdir')
    assert(new_filename.name == new_filename.filename_str + new_filename.extension_str)
    