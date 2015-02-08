import tornado.websocket
from models import users

chatters = {}

class ChatWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.user = int(self.get_secure_cookie("user"))
        chatters[self.user] = self
        print('Chat connected.')

    def on_message(self, input):
        print(input)
        # check all connections and notify the other matched user
        target = input['target']
        msg = input['msg']
        matches = users.matches(self.user)
        # target is chatting and is a match
        if target in chatters and chatters[target].user in matches:
            chatters[target].write_message('Match: ' + msg)
            self.write_message('You: ' + msg)

    def on_close(self):
        del chatters[self.user]

