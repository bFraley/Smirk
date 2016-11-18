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

class HTMLConstruct():
    def __init__(self, html_tagname):
        self.html_tagname = html_tagname
        self.__opentag = '<' + self.html_tagname + '>'
        self.__closetag = '</' + self.html_tagname + '>'
        self.__empty_element = self.__opentag + self.__closetag


    def __str__(self):
        return self.__empty_element
        