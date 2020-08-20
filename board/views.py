from django.shortcuts import render
from board import validation
from board import data_loader

def index(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    val_result = 1
    return render(request, 'login.html', {'val_result' : val_result})

def registration(request):
    val_result = 0
    return render(request, 'registration.html', {
        'val_result' : val_result
    })

def forgotPassword(request):
    return render(request, 'forgot_password.html')

def boards(request, board_id):
    return render(request, 'boards.html', {
        'board_id' : board_id,
    })

def posts(request, post_id):
    return render(request, 'posts.html', {
        'post_id' : post_id,
    })

def threads(request, thread_id):
    return render(request, 'threads.html', {
        'thread_id' : thread_id,
    })

def profile(request):
    return render(request, 'profile.html')

def processRegistration(request):
    request_data = {
        'username' : request.POST['username'],
        'email' : request.POST['email'],
        'phone' : request.POST['phone_number'],
        'password' : request.POST['password'],
        'retype_password' : request.POST['retype_password'],
    }
    val_result = validation.checkRetypedPassword(request_data['password'], request_data['retype_password'])
    if val_result == 1:
        data_loader.addUser(request_data)
        return render(request, 'profile.html', {'username': request_data['username']})
    return render(request, 'registration.html', {'val_result' : val_result})

def processLogin(request):
    login_data = {
        'email_or_phone' : request.POST['email_or_phone'],
        'password' : request.POST['password'],
    }

    val_result = data_loader.checkUser(login_data)
    if val_result == 1:
        return render(request, 'home.html')
    return render(request, 'login.html', {'val_result' : val_result})
