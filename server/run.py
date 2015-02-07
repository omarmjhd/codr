#!/usr/bin/env python3

import tornado.ioloop
import tornado.web

import api.login
import api.user

import config

application = tornado.web.Application([
    (r"/api/login", api.login.Handler),
    (r"/api/user/(?P<uid>[^\/]+)/?", api.user.UserHandler),
    (r"/api/like/(?P<target_id>[^\/]+)/?", api.user.LikeHandler),
    (r"/api/reject/(?P<target_id>[^\/]+)/?", api.user.RejectHandler),
    (r"/api/find/?", api.user.FindHandler),
    (r"/api/matches/?", api.user.MatchesHandler)
], cookie_secret=config.app_secret)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
