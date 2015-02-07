import tornado.websocket
from models import users

class NotificationsWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        user = users.get_user(int(self.get_secure_cookie("user")))
        print('Websockets connected.')

    def on_message(self, message):
        print('MATCH ------------')
        print(message)

    def on_close(self):
        pass

