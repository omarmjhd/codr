import tornado.websocket
from models import users

chatters = set()

class ChatWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.user = int(self.get_secure_cookie("user"))
        chatters.add(self)
        print('Chat connected.')

    def on_message(self, target_id):
        print('--------MATCH----------')
        print(self.user, target_id)
        # check all connections and notify the other matched user
        for n in notifiers:
            print(n.user, int(target_id))
            if n.user == int(target_id):
                user = users.get_user(self.user)
                n.write_message(user['name'])

    def on_close(self):
        notifiers.remove(self)

