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
class SmirkControlToken():
    pass

# Defines a comparison boolean token (is, not, and, or)
class SmirkComparisonToken():
    pass

# Defines an extension token that is bound/bindable to a value
class SmirkExtensionToken():
    pass

# Error based token keyword definition classes
# --------------------------------------------

# Defines developer defined error token
class SmirkDefineErrorToken():
    pass

# Defines Smirk implementation defined error token
class SmirkCoreErrorToken():
    pass
