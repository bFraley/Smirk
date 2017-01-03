"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: service_event.py

About: Generic service event type used to build many types of
service events. The ServicesProcessor manages ServiceEvent(s).
Service Events represent actions implemented in Smirk's core,
like ParseEvent, ReadEvent, WriteEvent, etc. All functionality
leads to an instance of an event that is processed by the 
ServicesProcessor"""


class ServiceEvent():
    def __init__(self, smirk_event_type):
        self.smirk_event_type = smirk_event_type


    def get_smirk_event_type(self):
        if isinstance(self.smirk_event_type, PreproccessedSmirkFile):
            self.event_type = "parser_process_event"
            