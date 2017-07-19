#!/usr/bin/env python
# -*- coding: utf-8 -*-

class index:
    def GET(self, app):
        app.header('Content-type', 'text/plain')
        return "Welcome!\n"
 
class hello:
    def GET(self, app, name):
        app.header('Content-type', 'text/plain')
        return "Hello %s!\n" % name
