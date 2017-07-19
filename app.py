#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urls import urls
from application import my_app
import route

wsgiapp = my_app(urls, route)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8086, wsgiapp)
 
    sa = httpd.socket.getsockname()
    print 'http://{0}:{1}/'.format(*sa)
    httpd.serve_forever()
