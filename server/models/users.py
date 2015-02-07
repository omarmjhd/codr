from pymongo import MongoClient

client = MongoClient()

db = client.codr

def add_user(id, gender, name, token, avatar_url):
    users = db.users
    users.insert(
        {'_id': id, 'name': name, 'access_token': token, 'avatar': avatar_url}
    )

def get_user(id):
    users = db.users
    return users.find_one({'_id' : id})

def make_match(a_id, b_id):

    users = db.users
    a = users.find_one({'_id': a_id})
    b = users.find_one({'_id': b_id})

    if not a.matches:
        a.matches = [b_id]
    if not b.matches:
        b.matches = [b_id]

    a.matches.append(a)
    b.matches.append(b)

