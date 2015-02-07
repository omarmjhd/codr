import tornado.web
from models import users

class UserHandler(tornado.web.RequestHandler):

    def get(self, uid):
        print(id)
        return users.get_user(uid)


class LikeHandler(tornado.web.RequestHandler):

    def get(self):
        id = self.get_argument('id')
        return users.like(id)

class RejectHandler(tornado.web.RequestHandler):

    def get(self):
        id = self.get_argument('id')
        return users.reject(id)

class FindHandler(tornado.web.RequestHandler):

    def get(self):
        id = self.get_argument('id')
        return users.get_potential(id)
