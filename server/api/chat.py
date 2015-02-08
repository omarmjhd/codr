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
        print(e)
        # check all connections and notify the other matched user
        target = int(e['target'])
        msg = e['msg']
        matches = dict(
            [(x['id'], x['name']) for x in users.get_matches(self.user)]
        )
        # target is chatting and is a match
        if target in chatters and chatters[target].user in matches:
            match = chatters[target].user
            chatters[target].write_message(matches[match] + ': ' + msg)
            self.write_message('You: ' + msg)

        # notify the match for a chat
        elif chatters[target].user in matches:
            for n in notifiers:
                if n.user == chatters[target].user:
                    user = users.get_user(self.user)
                    n.write_message(user['name'])


    def on_close(self):
        del chatters[self.user]

