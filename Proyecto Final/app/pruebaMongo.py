from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://betote:6hBzndMr3RLsBDFx@cluster0-3vp2d.mongodb.net/test?retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE')
db = client.test

class User(UserMixin):

    def __init__(self, email, name=None, is_admin=0):
        
        self.email = email
        self.name = name
        self.is_admin = is_admin

        self.id = None
        self.password = None
    
    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def set_id(self, id):
        self.id = id
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        print(self)
        db.userBlockChain.insert_one({'user_id': self.id, 'email': self.email, 'name':self.name, 'is_admin':self.is_admin, 'password': sel})

    def set_info(self, email, id):
        userInfo = db.userBlockChain.find_one({'email': email})

        if userInfo is not None:
            self.name = userInfo.get('name')
            self.is_admin = userInfo.get('is_admin')
            self.password = userInfo.get('password')
            self.id = id
    
    @staticmethod
    def get_by_id(id):
        return db.userBlockChain.find_one({'id': id})
    
    @staticmethod
    def get_by_email(email):
        return db.userBlockChain.find_one({'email': email})