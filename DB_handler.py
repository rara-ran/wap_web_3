from pyrebase import pyrebase
import json


class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def register(self,_id_,pw):
        self.db.child('user_info').child(_id_).set(pw)

    def login(self, _id, pw):
        users = self.db.child("user_info").get().val()
        try:
            userinfo = users[_id]
            if userinfo["pw"] == pw:
                return True
            else:
                return False
        except:
            return False
    

