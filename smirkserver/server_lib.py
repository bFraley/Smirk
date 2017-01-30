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

# Returns tuple of route, params
def get_request_route_and_params(request_input_string):
    both = request_input_string.split(' ')[1].split('?')
    return (both[0], both[1:])

# Returns list of tuples of key/values of params
def get_params_list(params_string):
    params_string = str(params_string[0])
    result = []

    # Get multiple url parameters
    if '&' in params_string:
        params = params_string.split('&')

        # Append tuples of url params key/values to result[]
        for par in params:

            if '=' in par:
                sides = par.split('=')
                result.append((sides[0], sides[1]))

    # There's a single url parameter
    else:
        if '=' in params_string:
            sides = params_string.split('=')
            result.append( (sides[0], sides[1]))


    return result
    
