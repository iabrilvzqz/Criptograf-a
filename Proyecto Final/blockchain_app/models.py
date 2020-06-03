from flask_login import UserMixin

users = []

class User(UserMixin):
    def __init__(self, number, passwd):
        self.id = number
        self.password = passwd

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def check_user(id):
        userInfo = db.userBlockChain.find_one({'user_id': int(id)})

        if userInfo != None:
            authUser = User(userInfo.get('user_id'), userInfo.get('password'))
        else:
            return None