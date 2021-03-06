"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: test_codegen.py

About: Tests for the following files.
    1. core/codegen_lib.py (Smirk implementation library)
    2. core/codegen.py (Smirk runtime script)
"""

from nose.tools import *
from core.codegen_lib import *

print('........runnning core/test_codegen.py')

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
    assert(new_html_attribute.get_result == 'name=""')

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

    # Helper 'init_two_paragraphs' defined below.
    # Tests for child <p> elements with innertext.
    init_two_paragraphs(wrapper_div)

    # Add new div child element with two
    # <p> grandchildren of wrapper-div
    new_child_div = HTMLConstruct('div')

    # Reuse class_attr from above
    new_child_div.add_attribute(class_attr)

    # Add paragraphs to new child div
    init_two_paragraphs(new_child_div)

    # Here we should now have a child div,
    # with two paragraphs that are then 
    # grandchildren of wrapper-div.
    wrapper_div.add_child_element(new_child_div)

    print(wrapper_div.get_full_element_result())


# CSS Constructs Tests
# --------------------

def test_CSSConstruct():
    selectors = ['h1']
    rules = {'color':'red'}
    new_css_block = CSSConstruct(selectors, rules)

def test_CSSSelectorConstruct():
    el_type = '.'
    el_name = 'some_element_class'

    new_css_selector_line = CSSSelectorConstruct(el_name, el_type)
    result = new_css_selector_line.get_full_selector_result()

    assert(result == '.some_element_class ')
    print(result)


def test_CSSAttributeConstruct():
    pass

# JS Constructs Tests
# -------------------


# File Name Constructs Tests
# --------------------------

def test_FileNameConstruct():
    new_filename = FileNameConstruct('test', file_extensions['html'])
    print(new_filename)

    new_filename.prepend('previousdir')
    assert(new_filename.name == new_filename.filename_str + new_filename.extension_str)


# Test Helper Functions for building HTML Construct elements.
# -----------------------------------------------------------

# Create two paragraphs and attach to a parent HTML element node.
def init_two_paragraphs(parent_element):
    assert(isinstance(parent_element, HTMLConstruct))

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
    parent_element.add_child_element(par1)
    parent_element.add_child_element(par2)



# Test Helper Functions for building CSS Construct elements.
# -----------------------------------------------------------



# Test Helper Functions for building JS Construct elements.
# -----------------------------------------------------------



# Test Helper Functions for building File Name Construct elements.
# -----------------------------------------------------------

