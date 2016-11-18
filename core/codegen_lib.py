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

# HTML
# ----------------------------------------------------------------------

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



# Smirk specific path and file extension utils.
# ----------------------------------------------------------------------

file_extensions = {
    'html': '.html',
    'css': '.css',
    'js': '.js'
}

# Construct a filename string object.
    # Requires a file name.
    # Extension is optional.
    # Slash direction is optional, for supporting Windows file systems.

class FileNameConstruct():
    def __init__(self, filename_str, extension_str=None, slash_direction=None):
        self.filename_str = filename_str
        self.extension_str = extension_str or None
        self.slash_direction = slash_direction
        self.name = self.get_full_filename()

    # Concat values and return full filename string.
    def get_full_filename(self):
        return self.filename_str + self.extension_str

    # Prepend string values to the filename for dirs.
    # Accepts optional value.
    # If not provided, a leading slash is prepended to the filename.
    def prepend(self, prepend_str):
        self.prepend_str = prepend_str or self.slash_direction

        if not self.prepend_str == self.slash_direction:
            self.prepend_str += self.slash_direction

        self.name = self.prepend_str + self.name


    def __str__(self):
        return self.name


