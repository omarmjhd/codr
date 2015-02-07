#!/usr/bin/env python3

import tornado.ioloop
import tornado.web

import api.login
import api.user

application = tornado.web.Application([
    (r"/api/login", api.login.Handler),
    (r"/api/user", api.user.UserHandler)
    (r"/api/like", api.user.LikeHandler)
    (r"/api/reject", api.user.RejectHandler)
    (r"/api/find", api.user.FindHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
