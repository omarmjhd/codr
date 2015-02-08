import tornado.websocket
from models import users

notifiers = set()

class NotificationsWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print(self.get_cookie('user'))
        self.user = int(self.get_secure_cookie("user"))
        notifiers.add(self)
        print('Notifications connected.')

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
        if self in notifiers:
            notifiers.remove(self)

