"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: smirk_lang_parse.py

About: Implements parser for Smirk template language.
"""

# The parser should only read, never modify users' source files.
# New, or 'smirk_production' directory source code files are opened
# for read/write modification and original sources don't need to 
# ship with production code repositories after building.

# An HTML source file that contains Smirk lang code to be parsed.
class SmirkUnparsedSourceFile(filepath_str, metadata_list=[]):
    def __init__(self):
        self.__filepath_str = filepath_str
        self.__metadata_list = metadata_list
        self.__linecount = 0
        self.__smirk_codeblock_count = 0
        self.__preprocess_data = {}

    def preprocess_smirkfile(self):
        # Unparsed source file preprocessing performed here.
        # Creates and returns PreprocessedSmirkFile object from
        # self.preprocess_data values.

        # preproccessed_result = PreprocessedSmirkFile(self.preprocess_data)    
        # return preprocessed_result
        pass

    def send_file_parser_event(self, preprocessed_smirkfile_obj):
        pass


# A preprocessed HTML file that contains Smirk lang code, 
# which is the resulting object produced by:
# SmirkUnparsedSourceFile.preprocess_smirkfile() - defined above.

class PreprocessedSmirkFile():
    def __init__(self):
        
