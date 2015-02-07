from pymongo import MongoClient

client = MongoClient()

db = client.codr
users = db.users

def add_user(_id, name, token, avatar_url):
    users.insert(
        {'_id': _id, 'name': name, 'access_token': token, 'avatar': avatar_url}
    )

def get_user(_id):
    return users.find_one({'_id' : _id})

def like(source_id, target_id):
    user = get_user(source_id)

    if not user.likes:
        user.likes = []

    user.likes.append(target_id)

    target = get_user(target_id)

    # return if they are a match
    return target.likes and source_id in target.likes

def get_matches(_id):
    user = get_user(source_id)

    matches = []
    if user.likes:
        for like in user.likes:
            target = get_user(like)
            if _id in target.likes:
                matches.append(like)

    return matches
