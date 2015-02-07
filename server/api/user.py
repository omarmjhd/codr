import tornado.web
from models import users

class UserHandler(tornado.web.RequestHandler):

    def get(self, uid):
        user = users.get_user(int(uid))
        print(user)
        return user


class LikeHandler(tornado.web.RequestHandler):

    def get(self, uid):
        return users.like(uid)

class RejectHandler(tornado.web.RequestHandler):

    def get(self, uid):
        return users.reject(uid)

class FindHandler(tornado.web.RequestHandler):

    def get(self, uid):
        return users.get_potential(uid)
