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

# import runtime_lib.services_processesor

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
        self.__preprocess_data = []
        self.__parserevent_data = []

    def preprocess_smirkfile(self):
        # Unparsed source file preprocessing performed here.
        # Creates and returns PreprocessedSmirkFile object from
        # self.preprocess_data values. The data values are a list
        # of blocks of Smirk code pulled from the original file,
        # with helper meta data about that line(s) associated with
        # each line / block of <smirk></smirk> tags.

        # preproccessed_result = PreprocessedSmirkFile(self.preprocess_data)    
        # return preprocessed_result
        pass


    # Send / emit a Smirk file parser event along with the 
    # preporocessed file object to be parsed.
    def send_file_parser_event(self, preprocessed_smirkfile_obj):
        assert(isinstance(preprocessed_smirkfile_obj, PreprocessedSmirkFile)
        
        # Spec for ServicesEvent parameters not implemented...
        # event_data = runtime_lib.ServicesEvent(preprocessed_smirkfile_obj) 

        # Register runtime services event notification,
        # and then the services processor references back to methods
        # in this library that call/start parsing operations.

        # runtime_lib.services_processesor.register_event_data(event_data)


# A preprocessed HTML file that contains Smirk lang code, 
# which is the resulting object produced by:
# SmirkUnparsedSourceFile.preprocess_smirkfile() - defined above.

class PreprocessedSmirkFile():
    def __init__(self, preprocess_data_obj):
        self.preprocess_data_obj = preprocess_data_obj

