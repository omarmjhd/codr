import tornado.websocket
import json
from models import users

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
        matches = [x['id'] for x in users.get_matches(self.user)]
        # target is chatting and is a match
        if target in chatters and chatters[target].user in matches:
            print('TARGET ACQUIRED.')
            print(msg)
            chatters[target].write_message('Match: ' + msg)
            self.write_message('You: ' + msg)

    def on_close(self):
        del chatters[self.user]

