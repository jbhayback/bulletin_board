from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.db.models import Q

from .status import Status
from .validation import FormValidation
from .authentication import CustomAuthentication

def index(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html', {
        'status' : Status.Success,
        'message' : None,
    })

def registration(request):
    return render(request, 'registration.html', {
        'status' : Status.Success,
        'message' : None,
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
    form_validator = FormValidation(request_data)
    User = get_user_model()
    val_result = form_validator.validate(User)
    if val_result['status'] == Status.Success:
        extra_data = {
            'username' : request.POST['username'],
            'phone' : request.POST['phone_number'],
        }
        User.objects.create_user(request_data['email'], request_data['password'], **extra_data)
        return render(request, 'profile.html', {'username': request_data['username']})
    return render(request, 'registration.html', val_result)

def processLogin(request):
    user_data = {
        'email_or_phone' : request.POST['email_or_phone'],
        'password' : request.POST['password'],
    }
    if request.POST['email_or_phone']:
        User = get_user_model()
        authenticator = CustomAuthentication()
        val_result = authenticator.authenticate(user_data, User)
        if val_result['status'] == Status.Success:
            return HttpResponseRedirect('home/')
    else:
        val_result = {
            'status' : Status.EmptyEmailOrPhone,
            'message' : 'Email of Phone has to be filled!',
        }

    return render(request, 'login.html', val_result)
    
