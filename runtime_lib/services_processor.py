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
        if (isinstance(service_event_obj, ServiceEvent)):

            if (service_event_obj.event_type == "parser_proces_event"):
                # return new ParserProcess
                return ParserProcess(service_event_obj);


class Processor():
    def __init__(self):
        self.event_count = 0
        self.linear_que = []
        self.selective_que = []
        self.warnings = []
        self.errors = []
        self.step_mode = false
        self.log_mode = false
        self.status = 0

    # Return and print processor values, called by methods below
    def view_by_list(self, processor_item):
        if self.log_mode:
            for item in processor_item:
                print(processor_item)

        return processor_item

    def view_state(self):
        state = [
            '\nProcessor State Report\n********************',
            'Event Count: {}\n'.format(self.event_count),
            'Linear Events: {}\n'.format(len(self.linear_que),
            'Selective Events: {}\n'.format(len(self.selective_que),
            'Warnings: {}\n'.format(len(self.warnings),
            'Errors: {}\n'.format(len(self.errors)]

        for line in state:
            print(line)

    def view_events(self):
        pass

    def view_linear_que(self):
        if (self.log_mode):
            for linear_event in self.linear_que:
                print(linear_event)

        return self.linear_que

    def view_selective_que(self):
        pass

    def view_warnings(self):
        pass

    def view_errors(self):
        pass
