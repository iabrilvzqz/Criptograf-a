from werkzeug.security import generate_password_hash

import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://betote:6hBzndMr3RLsBDFx@cluster0-3vp2d.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
db = client.test

db.userBlockChain.insert_one({'user_id': 0, 'password': generate_password_hash('admin'), 'isAdmin': 1})
db.userBlockChain.insert_one({'user_id': 1, 'password': generate_password_hash('employee1'), 'isAdmin': 0})
db.userBlockChain.insert_one({'user_id': 2, 'password': generate_password_hash('employee2'), 'isAdmin': 0})
db.userBlockChain.insert_one({'user_id': 3, 'password': generate_password_hash('employee3'), 'isAdmin': 0})
db.userBlockChain.insert_one({'user_id': 4, 'password': generate_password_hash('employee4'), 'isAdmin': 0})