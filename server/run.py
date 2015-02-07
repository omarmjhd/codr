#!/usr/bin/env python3

import tornado.ioloop
import tornado.web

import api.login

application = tornado.web.Application([
    (r"/api/login", api.login.Handler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
