import tornado.web
from models import users

class Handler(tornado.web.RequestHandler):


    def get(self):
        id = self.get_argument('id')

        return users.get_user(id)


