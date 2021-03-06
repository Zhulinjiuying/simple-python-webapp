#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class my_app:
    headers = []

    def __init__(self, urls, route):
        self._urls = urls
        self._route = route

    def __call__(self, environ, start_response):
        self._status = '200 OK' 
        del self.headers[:] 
 
        result = self._delegate(environ)
        start_response(self._status, self.headers)
 
        if isinstance(result, basestring):
            return iter([result])
        else:
            return iter(result)

    def _delegate(self, environ):
        path = environ['PATH_INFO']
        method = environ['REQUEST_METHOD']

        for pattern, name in self._urls:
            m = re.match('^' + pattern + '$', path)
            if m:
                args = m.groups()
                funcname = method.upper()
                clsname = 'self._route.' + name
                try:
                    cls = eval(clsname)()
                    if hasattr(cls, funcname):
                        func = 'cls.'+ funcname
                        return eval(func)(self, *args)
                except ArithmeticError:
                    pass
        return self._notfound()

    def _notfound(self):
        self._status = '404 Not Found'
        self.header('Content-type', 'text/plain')
        return "Not Found\n"

    @classmethod
    def header(cls, name, value):
        cls.headers.append((name, value))
