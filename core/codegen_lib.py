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
        self.__attributes = []
        self.__innertext_value = ''
        self.__child_nodes = []
        self.get_result = self.get_full_element_result()
        self.result = ''

        # Public assignments for development tests.
        self.test_attributes = self.__attributes
        self.test_child_nodes = self.__child_nodes


    # Add child HTML element nodes.
    def add_child_element(self, html_obj):
        assert(isinstance(html_obj, HTMLConstruct))
        self.__child_nodes.append(html_obj)


    # Add attribute name=value strings to HTML tags.
    def add_attribute(self, attribute_obj):
        assert(isinstance(attribute_obj, HTMLAttributeConstruct))
        self.__attributes.append(attribute_obj)


    # Add inner text to an HTML element.
    # Concats to any existing inner text, unless optional [replace] boolean is True. 
    def add_innertext(self, innertext_obj, replace=False):
        assert(isinstance(innertext_obj, HTMLInnerTextConstruct))

        if not replace:
            self.__innertext_value += str(innertext_obj)
        else:
            self.__innertext_value = str(innertext_obj)


    # Get count of inner child HTML element nodes.
    def get_child_count(self):
        return len(self.__child_nodes)


    # Return full completed HTML element node string.
    def get_full_element_result(self):

        # self.__opentag remains unaltered, preserving the plain tag.
        open_tag = self.__opentag

        # Amount of attributes.
        attr_count = len(self.__attributes)
        spacing = ' '

        # If tag has attrubutes.
        if attr_count > 0: 
            # Insert space before attributes.
            open_tag = list(self.__opentag)
            open_tag.insert(-1, spacing) 

            for attr in self.__attributes:

                # Don't add a space on final attrubute before closing '>' on tag.
                if self.__attributes.index(attr) == attr_count - 1:
                    spacing = ''

                open_tag.insert(-1, attr.result + spacing)

            open_tag = ''.join(open_tag)

        # If no children nodes...
        # Concat open tag, attributes, inner text value, and closing tag.

        if self.get_child_count() < 1:
            self.result = open_tag + self.__innertext_value + self.__closetag
        else:
            parent_wrapper = open_tag + self.__innertext_value

            # Recursive concat children and grandchildren HTML nodes.
            for child_element in self.__child_nodes:
                parent_wrapper += ('\n    ' + child_element.get_full_element_result())

            self.result = parent_wrapper + self.__closetag
        
        return self.result


    def __str__(self):
        return self.result


# Construct a partial, or empty HTML attribute object.
class HTMLAttributeConstruct():
    def __init__(self, attribute_name, assign_val=False):
        self.attribute_name = attribute_name
        self.assign_val = assign_val
        self.__equal_str = '='
        self.__quote_str = '"'
        self.__equal_str_plus_quote = '="'
        self.__empty_attribute = self.attribute_name + '=""'
        self.get_result = self.get_full_attribute_result()
        self.result = ''

    def get_full_attribute_result(self):
        if self.assign_val:
            self.result = self.attribute_name + self.__equal_str_plus_quote \
            + self.assign_val + self.__quote_str
        else:
            self.result = self.__empty_attribute

        return self.result

    def __str__(self):
        return self.result


# Construct a partial, empty, or defined HTML innerText string object.
class HTMLInnerTextConstruct():
    def __init__(self, content_str=""):
        self.content_str = content_str

    def __str__(self):
        return self.content_str


# CSS
# ----------------------------------------------------------------------

#Construct a CSS style definition code block.
# Accepts list of selectors, and dictionary values of rules.
class CSSConstruct():
    def __init__(self, selector_list=[], rule_dict={}):

        assert(isinstance(selector_list, list))
        assert(isinstance(rule_dict, dict))

        self.selector_list = selector_list
        self.rule_dict = rule_dict

        self.__LCURL = '{'
        self.__RCURL = '}'
        self.__DOT = '.'
        self.__HASH = "#"
        self.__COMMA = ','
        self.__COMMASPC = ', '
        self.__COLON = ":",
        self.__SEMICOLON = ';'
        self.__topcurl = self.__LCURL + '\n'
        self.__botcurl = self.__RCURL + '\n'

        self.__valid_html_selector_list = False
        self.__valid_userdef_selector_list = False
        self.__valid_style_attributes_list = False
        self.__valid_style_rules_list = False

        self.__selectors_line = ''
        self.__rules_values_lines = ''
        self.get_result = self.get_full_css_block_result()
        self.result = ''

    # Add a CSS selector to this block of CSS
    def add_selector_name(self, selector_obj):
        self.selectors.append(selector_obj)

    # Assign new style rule and value to rule_dict of this CSS block.
    def add_style_attribute(self, style_attr_obj):
        rule_dict[style_attr_obj.attr_name] = style_attr_obj.attr_value

    # Output string line of the selectors, e.g. "h1, h2, h3 {\n"
    def concat_selectors_line(self):
        line_result = ''
        selector_count = len(self.selector_list)

        for selector in self.selector_list:

            # Don't add comma after last selector, just a space
            if self.selector_list.index(selector) == selector_count - 1:
                line_result += selector + ' '
            else:
                line_result += selector + self.__COMMASPC

        return line_result

    # Output lines of the style attributes/values, e.g. "color: red;\n"
    def concat_attributes_lines(self):
        line_result = ''

        for k, v in self.rule_dict.items():

            print(k)
            print(v)
            newline = "\n{}{} {}{}".format(str(k), self.__COLON, str(v), self.__SEMICOLON)
            line_result += newline
             
        return line_result


    def get_full_css_block_result(self):
        self.result = self.concat_selectors_line() \
            + self.__topcurl + self.concat_attributes_lines() \
            + '\n' + self.__botcurl

        return self.result


# Output CSS selector code line up to open curly brace' 
class CSSSelectorConstruct():
    def __init__(self, selector_name, selector_type=''):
        self.selector_type = selector_type
        self.selector_name = selector_name

        # TODO: Need a mechanism for passing in prefix/pseudo types.
        self.__prefix = self.selector_type
        self.__pseudo = ''
        self.get_result = self.get_full_selector_result()
        self.result = ''

    def get_full_selector_result(self):
        self.result = self.__prefix + self.selector_name + ' '
        return self.result

    def __str__(self):
        return self.result


class CSSAttributeConstruct():
    def __init__(self, atrr_name, attr_val):
        self.__attr_name = attr_name
        self.__attr_val = attr_val
        self.result = (self.__attr_name, self.__attr_val)

    def __str__(self):
        return  self.result

            
# JavaScript
# ----------------------------------------------------------------------
# Reminder that in this library (codegen_lib.py), is not Smirk's implementation of it's
# front end JavaScript features. Here we are defining helper classes for the purpose 
# of generating basic JavaScript code constructs.

# Smirk template code is parsed into a que system that outputs
# an intermediate representation of the source code to generate.
# Then, the class types and methods are used to generate and write code to file.



































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
    def __init__(self, filename_str, extension_str=None, slash_direction=''):
        self.filename_str = filename_str
        self.extension_str = extension_str or None
        self.slash_direction = slash_direction or '/'
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

        self.filename_str = self.prepend_str + self.filename_str
        self.name = self.get_full_filename()


    def __str__(self):
        return self.name
