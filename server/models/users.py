from pymongo import MongoClient

client = MongoClient()

db = client.codr
users = db.users

def add_user(_id, name, token, avatar_url, languages):
    users.insert(
        {'_id': _id,
         'name': name,
         'access_token': token,
         'avatar': avatar_url,
         'languages':languages
        }
    )

def get_user(_id):
    return users.find_one({'_id' : _id})

def like(source_id, target_id):
    user = get_user(source_id)

    if not user:
        raise ValueError('No user with id %d found' % (source_id, ))

    if not user.likes:
        user.likes = []

    user.likes.append(target_id)

    target = get_user(target_id)

    if not target:
        raise ValueError('No user with id %d found' % (target_id, ))

    # return if they are a match
    return target.likes and source_id in target.likes

def reject(source_id, target_id):
    user = get_user(source_id)

    if not user:
        raise ValueError('No user with id %d found' % (source_id, ))

    if not user.rejects:
        user.rejects = []

    user.rejects.append(target_id)

def get_matches(_id):
    user = get_user(_id)

    if not user:
        raise ValueError('No user with id %d found' % (_id, ))

    matches = []
    if user.likes:
        for like in user.likes:
            target = get_user(like)
            if _id in target.likes:
                matches.append(like)

    return matches

def get_potential(_id):

    for user in users:
        if not user.matches:
            user.matches = []
        if not user.rejects:
            user.rejects = []
        if not _id in user.rejects and not _id in user.matches:
            return user

    return None
