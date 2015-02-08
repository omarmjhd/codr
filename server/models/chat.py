from pymongo import MongoClient

client = MongoClient()

db = client.codr
chat = db.chat

def get_chat(a, b):
    return chat.find(
        {'or' :
            [
                {'and' : [{'author':b},{'target':a}]},
                {'and' : [{'author':a},{'target':b}]}
            ]
        }
    )

def add_msg(a, b, msg):
    db.chat.insert({'author':a,'target':b,'content':msg})


