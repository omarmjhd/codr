import tornado.websocket
import json
from models import users
from models import chat
from api.notifications import notifiers

chatters = {}

class ChatWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.user = int(self.get_secure_cookie("user"))
        self.target = None
        chatters[self.user] = self
        print('Chat connected.')

    def on_message(self, e):
        e = json.loads(e)
        # check all connections and notify the other matched user
        self.target = int(e['target'])

        print(chat.get_chat(self.user, self.target))

        msg = e['msg']
        matches =  [x['id'] for x in users.get_matches(self.user)]
        author = users.get_user(self.user)
        # target is chatting and is a match and is chatting the same person
        if (self.target in chatters
            and self.target in matches
            and chatters[self.target].target == self.user):
            print(e)
            chatters[self.target].write_message(author['name'] + ': ' + msg)

        # otherwise send them an alert
        elif self.target in notifiers and self.target in chatters:
            chatters[self.target].write_message(author['name'] + ': ' + msg);

        chat.add_msg(self.user, self.target, msg)
        self.write_message('You: ' + msg)

    def on_close(self):
        if self.user in chatters:
            del chatters[self.user]

