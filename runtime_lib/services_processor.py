"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: runtime_lib/services_processor.py

About: An event based function call processor for 
directing Smirk's core runtime features.
"""

from core.smirk_lang_parse import ParserProcess
from service_event import ServiceEvent

# on parse event registration
# parser_service.parse()

class ServicesProcess():
    def __init__(self):
        pass

    def init_new_event(service_event_obj):
        assert(isinstance(service_event_obj, ServiceEvent))
        pass
