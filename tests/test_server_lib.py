"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: test_smirk_lang.py

About: Tests for smirkserver/server_lib.py
"""

print('........runnning core/test_server_lib.py')

from nose.tools import *
from smirkserver.server_lib import *

def test_cache_file():
    pass

def test_get_cached_file():
    pass

def test_get_request_route_and_params():
    pass

def test_get_params_list():
    pass

def test_get_explicit_route_paths():
    routes = get_explicit_route_paths(['/a', '/b', '/ab/c'])
    assert(isinstance(routes, list) and len(routes) == 3)

def test_explicit_route_exists():
    assert(explicit_route_exists('/home', ['/home']))
    assert(explicit_route_exists('/12', ['ab12', '12']) == False)
