import tornado.websocket
from models import users

class NotificationWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        user = users.get_user(int(self.get_secure_cookie("user")))
        print(user)

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        pass

