from werkzeug.security import generate_password_hash
import hashlib

import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://betote:6hBzndMr3RLsBDFx@cluster0-3vp2d.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
db = client.test

db.userBlockChain.insert_one({'user_id': int(hashlib.md5("juan@mallchain.com".encode()).hexdigest()[:8], 16), 'name': 'Juan Pérez' ,'email': 'juan@mallchain.com', 'password': generate_password_hash('admin'), 'is_admin': 1, 'objectID': None})
db.userBlockChain.insert_one({'user_id': int(hashlib.md5("victoria@mallchain.com".encode()).hexdigest()[:8], 16), 'name': 'Victoria Rodríguez' ,'email': 'victoria@mallchain.com', 'password': generate_password_hash('employee1'), 'is_admin': 0, 'objectID': None})
db.userBlockChain.insert_one({'user_id': int(hashlib.md5("rodrigo@mallchain.com".encode()).hexdigest()[:8], 16), 'name': 'Rodrigo López' ,'email': 'rodrigo@mallchain.com', 'password': generate_password_hash('employee2'), 'is_admin': 0, 'objectID': None})
