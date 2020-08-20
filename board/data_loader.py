from .models import Users

def addUser(user_data):
    user = Users()
    user.username = user_data['username']
    user.email = user_data['email']
    user.phone_number = user_data['phone']
    user.password = user_data['password']
    user.user_role = '2'
    user.save()

def checkUser(user_data):
    users = Users.objects.all()
    for user in users:
        if user.email == user_data['email_or_phone'] or user.phone_number == user_data['email_or_phone']:
            # if user.password == user_data['password']:
                return 1
    
    return -1
