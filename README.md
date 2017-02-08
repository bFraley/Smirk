# Smirk

Proof of concept exploratory work in web framework design and implementation.

To tinker with Smirk: clone, use Python3 and virtualenv/virtualenvwrapper, `pip install -r requirements.txt`

Run the dev server: `python3 smirkserver/run.py`

Run the tests from project root dir with `nosetests -s`

Some design notes:

`core/` - contains core implementation files. 

`core_adapters/` - adapters can be seen as miniature APIs that delegate communication and pass values between core modules and the `core/` functionality.

`core_modules/` - larger core Smirk features available to users and `core/` through APIs

`runtime_lib/` - A Smirk application's runtime is based on the idea of service events that are processed by a services processor. Every piece of functionality ends up as a service event type that one or many services processors handle.