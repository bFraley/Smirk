"""
Smirk - Web Application Framework
Copyright (c) 2016 Brett Fraley

Source Repository
https://github.com/bFraley/Smirk

MIT License
https://github.com/bFraley/Smirk/blob/master/LICENSE

File: project-source-file-copyright.py

About: Defines Class for defining and generating meta information
as comments for Smirk users' projects' source files.
"""

class ProjectSourceFileCopyright():
    def __init__(self):
        self.project_name = ''
        self.project_version = ''
        self.project_description = ''
        self.project_url = ''
        self.copyright_text = ''
        self.license_text = ''
        self.license_url = ''
        self.author_names = []
        