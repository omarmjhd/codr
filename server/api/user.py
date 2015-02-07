import tornado.web
from models import users

class UserHandler(tornado.web.RequestHandler):

    def get(self, uid):
        user = users.get_user(uid)
        print(user)
        self.write(user)


class LikeHandler(tornado.web.RequestHandler):

    def get(self, uid):
        self.write(users.like(uid))

class RejectHandler(tornado.web.RequestHandler):

    def get(self, uid):
        self.write(users.reject(uid))

class FindHandler(tornado.web.RequestHandler):

    def get(self, uid):
        self.write(users.get_potential(uid))
