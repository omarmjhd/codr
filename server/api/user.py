import json
import tornado.web
from models import users

class UserHandler(tornado.web.RequestHandler):

    def get(self, uid):
        user = users.get_user(int(uid))
        self.write(json.dumps(user))


class LikeHandler(tornado.web.RequestHandler):

    def get(self, uid):
        self.write(json.dumps(users.like(int(uid))))

class RejectHandler(tornado.web.RequestHandler):

    def get(self, uid):
        self.write(json.dumps(users.reject(int(uid))))

class FindHandler(tornado.web.RequestHandler):

    def get(self, uid):
        self.write(json.dumps(users.get_potential(int(uid))))
