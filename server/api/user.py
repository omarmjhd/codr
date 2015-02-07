import json
import tornado.web
from models import users
import datetime
import re

class UserHandler(tornado.web.RequestHandler):

    def get(self, uid):
        user = users.get_user(int(uid))
        self.write(json.dumps(user))


class LikeHandler(tornado.web.RequestHandler):

    def get(self, source_id, target_id):
        self.write(json.dumps(users.like(int(source_id), int(target_id))))

class RejectHandler(tornado.web.RequestHandler):

    def get(self, source_id, target_id):
        self.write(json.dumps(users.reject(int(source_id), int(target_id))))

class FindHandler(tornado.web.RequestHandler):

    def get(self, uid):
        user = users.get_potential(int(uid))
        date = datetime.datetime(*map(int, re.split('[^\d', user['updated_at'])[:-1]))
        diff = datetime.now() - date
        user['updated_at'] = str(diff.days) + " days ago"
        self.write(json.dumps(user))
