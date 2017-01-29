"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: smirk_lang.py

About: Defines grammar and syntax for Smirk template language.
"""

# Smirk template code is written within <smirk> tags in HTML files.
# Smirk's template language generates JavaScript, implementing a basic 
# front end web development framework, while also providing language
# features that interace with Smirk's server-side API's, Python, and
# database management systems.

# Defines Smirk tag tokens.
class SmirkTemplateTag():
    def __init__(self):
        self.__OPEN = '<smirk>'
        self.__CLOSE = '</smirk>'

    def open_token(self):
        return self.__OPEN

    def close_token(self):
        return self.__CLOSE

    def __str__(self):
        return self.open_token() + self.close_token()


# Defines a control logic token (for, if, else)
# Accepts the literal token string eg: 'if', 'for', 'every'

# Accepts expression pattern type from explicit
# list of defined grammar patterns.
        # Examples:
        # (var in list)
        # (every (key, value) of object),
        # (only (key, value) of object)

class SmirkControlToken():
    def __init__(self, token_str, expression_type_pattern):
        self.token_str = token_str
        self.expression_type_pattern = []

        # Implementation type reference for SmirkControlToken
        self.__SMIRKTOKENTYPE = 'ControlToken'
        
        # An explicit s-expression output pattern for parsing.
        self.__parse_pattern_output = ''

        # Generic pattern for handling error messages
        # for syntax rules of this token type.
        self.__syntax_error_reference_pattern = ''

    def generate_parse_pattern_output(self):
        pass

    def generate_syntax_error_reference(self):
        pass


# Defines a comparison boolean token (is, not, and, or)
class SmirkComparisonToken():
     def __init__(self, token_str):
        self.token_str = token_str
        self.left_type_and_val = []
        self.right_type_and_val = []

        # Implementation type reference for SmirkControlToken
        self.__SMIRKTOKENTYPE = 'ComparisonToken'
        
        # An explicit s-expression output pattern for parsing.
        self.__parse_pattern_output = [
            ('LTYPE', 'LTYPE'),
            ('LVAL', 'LVAL'),
            ('COMP_OP', 'COMP_OP'),
            ('RTYPE', 'RTYPE'),
            ('RVAL', 'RVAL'),
        ]

        # Generic pattern for handling error messages
        # for syntax rules of this token type.    
        self.__syntax_error_reference_pattern = ''

        def generate_parse_pattern_output(self):
            pass

        def generate_syntax_error_reference(self):
            pass

# Defines an extension token that is bound/bindable to a value,
# is a base implementation type for user defined variables.

# eg: a = 1 would call new SmirkExtensionToken('a', number, 1)

class SmirkExtensionToken():
    def __init__(self, namespace_name, value_type, init_default_value):
        self.namespace_name = namespace_name
        self.value_type = value_type
        self.init_default_value = init_default_value




# Error based token keyword definition classes
# --------------------------------------------

# Defines Smirk implementation defined error token
class SmirkCoreErrorToken():
    def __init__(self, error_type, error_msg, misc=null):
        self.error_type = error_type
        self.error_msg - error_msg
        self.misc = misc

    def __str__(self):
        return 'Error Type: {}\nError Message:{} - {}'.format(self.error_type, self.error_msg, self.misc);


# Defines developer defined error token
class SmirkDefineErrorToken(SmirkCoreErrorToken):
    def __init__(self, user_error_definition):
        self.user_error_definition = user_error_definition


# ------------------------------------------------------------------------------------------------
# SmirkCoreLib contains functions available to Smirk lang Token types and language constructs above.
# These are functional helpers and operators that support logic and value manipulation with Smirk code.

class SmirkCoreLib():
    def __init__(self):

    # Arithmetic

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mult(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

    def mod(self, n1, n2):
        return n1 % n2

    # String Manipulation

    def cat(self, s1, s2):
        return s1 + s2

    def instring(needle, hay):
        return True if needle in hay else False

    def are_exact_names(s1, s2):
        return True if s1 == s2 else False

    def are_exact_values(v1, v2):
        return True if v1 == v2 and type(v1) == type(v2) else False

    # Numeric Formatting and Type Conversions






















