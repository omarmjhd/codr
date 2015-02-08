import tornado.websocket
from models import users

notifiers = {}

class NotificationsWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.user = int(self.get_secure_cookie("user"))
        notifiers[self.user] = self
        print('Notifications connected.')

    def on_message(self, target_id):
        print('--------MATCH----------')
        print(self.user, target_id)
        # check all connections and notify the other matched user
        if target_id in notifiers:
            user = users.get_user(self.user)
            notifiers[target_id].write_message(user['name'])

    def on_close(self):
        if self in notifiers:
            notifiers.remove(self)

