import tornado.websocket
from models import users

notifiers = set()

class NotificationsWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.user = int(self.get_secure_cookie("user"))
        notifiers.add(self)
        print('Websockets connected.')

    def on_message(self, target_id):
        print('--------MATCH----------')
        print(self.user, target_id)
        # check all connections and notify the other matched user
        for n in notifiers:
            print(n.user, int(target_id))
            if n.user == int(target_id):
                n.write_message(self.user)

    def on_close(self):
        notifiers.remove(self)

