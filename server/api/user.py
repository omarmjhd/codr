import json
import tornado.web
import config
from models import users
import datetime
import re

class BaseHandler(tornado.web.RequestHandler):

    def get_current_user(self):
        return int(self.get_secure_cookie("user"))

class UserHandler(BaseHandler):

    def get(self):
        user = users.get_user(self.get_current_user())
        if not user: return
        self.write(json.dumps(user))


class LikeHandler(BaseHandler):

    def get(self, target_id):
        self.write(
            json.dumps(users.like(self.get_current_user(), int(target_id)))
        )

class RejectHandler(BaseHandler):

    def get(self, target_id):
        self.write(json.dumps(
            users.reject(self.get_current_user(), int(target_id)))
    )

class FindHandler(BaseHandler):

    def get(self):
        user = users.get_potential(self.get_current_user())
        if not user: return

        # write a secure cookie to prevent spoofing
        self.set_secure_cookie("target", str(user['_id']))

        date = datetime.datetime(*map(int, re.split('[^\d]', user['updated_at'])[:-1]))
        diff = datetime.datetime.now() - date
        user['updated_at'] = str(diff.days) + " days ago"
        self.write(json.dumps(user))

class MatchesHandler(BaseHandler):

    def get(self):
        self.write(json.dumps(users.get_matches(self.get_current_user())))

class TokenHandler(BaseHandler):

    def get(self):
        self.write(config.gh_id)
