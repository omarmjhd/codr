import tornado.web
from models import users

class UserHandler(tornado.web.RequestHandler):

    def get(self, uid):
        user = users.get_user(uid)
        print(user)
        return user


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
