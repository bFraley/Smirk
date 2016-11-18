"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: codegen_lib.py

About: Provides utilities for Smirk specific code generation of
HTML, CSS, JS, and other languages and source file formats. 
"""

# Construct a partial, or empty HTML element node object. 
class HTMLConstruct():
    def __init__(self, html_tagname):
        self.html_tagname = html_tagname
        self.__opentag = '<' + self.html_tagname + '>'
        self.__closetag = '</' + self.html_tagname + '>'
        self.__empty_element = self.__opentag + self.__closetag


    def __str__(self):
        return self.__empty_element


# Construct a partial, or empty HTML attribute object.
class HTMLAttributeConstruct():
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name
        self.__equal_str = '='
        self.__quote_str = '"'
        self.__equal_str_plus_quote = '="'
        self.__empty_attribute = self.attribute_name + '=""'

    def __str__(self):
        return self.__empty_attribute


# Construct a partial, empty, or defined HTML innerText string object.
class HTMLInnerTextConstruct():
    def __init__(self, content_str):
        self.content_str = content_str or ""

    def __str__(self):
        return self.content_str

