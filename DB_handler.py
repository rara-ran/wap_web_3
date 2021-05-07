from pyrebase import pyrebase


class DBModule:
    def __init__(self):
        config = {
            "apiKey": "AIzaSyCFj9VQyRjRoqHDX_ZtFhS2h2JwGHWbAPA",
            "authDomain": "wap-web-project.firebaseapp.com",
            "databaseURL": "https://wap-web-project-default-rtdb.firebaseio.com",
            "projectId": "wap-web-project",
            "storageBucket": "wap-web-project.appspot.com",
            "messagingSenderId": "283455518398",
            "appId": "1:283455518398:web:9118aedeeb91e69b0c50ef"
        }

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
    

