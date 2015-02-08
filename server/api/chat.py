import tornado.websocket
import json
from models import users
from api.notifications import notifiers

chatters = {}

class ChatWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        if self.get_secure_cookie("user"):
            self.user = int(self.get_secure_cookie("user"))
        else:
            self.user = None
        self.target = None
        chatters[self.user] = self
        print('Chat connected.')

    def on_message(self, e):
        e = json.loads(e)
        # check all connections and notify the other matched user
        self.target = int(e['target'])
        msg = e['msg']
        matches =  [x['id'] for x in users.get_matches(self.user)]
        # target is chatting and is a match
        if self.target in chatters and self.target in matches:
            author = users.get_user(self.user)
            chatters[self.target].write_message(author['name'] + ': ' + msg)
            self.write_message('You: ' + msg)

        # notify the match for a chat
        else:
            for n in notifiers:
                if n.user == self.target:
                    user = users.get_user(self.user)
                    self.write_message('You: ' + msg)
                    n.write_message(user['name'])


    def on_close(self):
        if self.user in chatters:
            del chatters[self.user]

