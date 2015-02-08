import tornado.websocket
import json
from models import users
from api.notifications import notifiers

chatters = {}

class ChatWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.user = int(self.get_secure_cookie("user"))
        chatters[self.user] = self
        print('Chat connected.')

    def on_message(self, e):
        e = json.loads(e)
        # check all connections and notify the other matched user
        target = int(e['target'])
        msg = e['msg']
        matches =  [x['id'] for x in users.get_matches(self.user)]
        print(target)
        print(chatters)
        print(self.user)
        # target is chatting and is a match
        if target in chatters and target in matches:
            print(e)
            author = users.get_user(self.user)
            chatters[target].write_message(author['name'] + ': ' + msg)
            self.write_message('You: ' + msg)

    def on_close(self):
        if self.user in chatters:
            del chatters[self.user]

