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
        self.original_filestring = self.return_filestring()
        self.filestring = ''

    def return_filestring(self):
        src = open(self.__filepath_str, 'r')
        src_read = src.read()
        src.close()
        return src_read

    def preprocess_smirkfile(self):
        # Unparsed source file preprocessing performed here.
        # Creates and returns PreprocessedSmirkFile object from
        # self.preprocess_data values. The data values are a list
        # of blocks of Smirk code pulled from the original file,
        # with helper meta data about that line(s) associated with
        # each line / block of <smirk></smirk> tags.
        
        filestring = self.filestring
        tag1_index = filestring.index('<smirk>') + 6
        tag2_index = filestring[s1:].index('</smirk>') + 7
        tag_range = tag1 + tag2
        extracted_block = filestring[tag1:tag_range]

        self.__preprocess_data.append(extracted_block)
        self.__smirk_codeblock_count += 1

        # Removes the extracted smirk code block and rejoins filestring. 
        filestring = filestring.split(extracted_block)
        filestring = ''.join(filestring)

        # If done, return PreprocessedSmirkFile object, else recursive call.
        if not '<smirk>' in filestring and not '</smirk' in filestring:
            preproccessed_result = PreprocessedSmirkFile(self.__preprocess_data)    
            return preprocessed_result
        else:
            self.preprocess_smirkfile()


    # Send / emit a Smirk file parser event along with the 
    # preporocessed file object to be parsed.
    def send_file_parser_event(self, preprocessed_smirkfile_obj):
        assert(isinstance(preprocessed_smirkfile_obj, PreprocessedSmirkFile))
        
        # Spec for ServicesEvent parameters not implemented...
        event_data = runtime_lib.ServiceEvent(preprocessed_smirkfile_obj) 

        # Register runtime services event notification,
        # and then the services processor references back to methods
        # in this library that call/start parsing operations.

        # runtime_lib.services_processesor.register_event_data(event_data)


# A preprocessed HTML file that contains Smirk lang code, 
# which is the resulting object produced by:
# SmirkUnparsedSourceFile.preprocess_smirkfile() - defined above.


class PreprocessedSmirkFile():
    def __init__(self, smirk_codeblock_list):
        self.smirk_codeblock_list = smirk_codeblock_list


# A ParserProcess is instantiated by runtime_lib/services_processor.py
class ParserProcess():
    def __init__(self):
        pass

