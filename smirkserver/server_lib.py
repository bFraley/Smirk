"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: server_lib.py

About: Library for implementing Smirk's basic development HTTP server
"""

def cache_file(cache_list, filename):
    with open(filename, 'r') as f:
        cache_list.append(f.read())
        return cache_list[-1]

def get_cached_file(cache_list, filename):
    for file in cache_list:
        if file.filename == filename:
            return file.content
        else:
            return false


def get_request_route():
    pass

def get_request_params():
    pass
