from .models import Users

def addUser(user_data):
    user = Users()
    user.username = user_data['username']
    user.email = user_data['email']
    user.password = user_data['password']
    user.save()
