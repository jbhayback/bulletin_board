from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.shortcuts import redirect

from rest_framework.authtoken.models import Token

from .status import Status
from .validation import FormValidation
from .authentication import CustomAuthentication

def index(request):
    return render(request, 'login.html')

def home(request):
    if 'user' in request.session:
        user = request.session['user']
        return render(request, 'home.html', {'user':user})
    render(request, 'login.html')

def login(request):
    if 'user' in request.session:
        user = request.session['user']
        return HttpResponseRedirect('/home/')
    return render(request, 'login.html', {
        'status' : Status.Success,
        'message' : None,
    })

def registration(request):
    if 'user' in request.session:
        user = request.session['user']
        return HttpResponseRedirect('/home/')
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
        user = User.objects.create_user(request_data['email'], request_data['password'], **extra_data)
        token = Token.objects.get(user=user).key
        processEmailActivation(request_data['email'], token)
        return render(request, 'profile.html', {'username': request_data['username'], 'token': token})
    return render(request, 'registration.html', val_result)

def processEmailActivation(email, token):
    msg_html = render_to_string('activation_mail.html', {'token':token})
    send_mail('Account Activation', 'Please activate your account!', '', [email], html_message=msg_html)

def activation(request, token_id):
    try:
        token = Token.objects.get(key=token_id)
    except ObjectDoesNotExist:
        return render(request, 'unauthorize.html')
    user_data = get_user_model()
    user = user_data.objects.get(email=token.user)
    user.is_active = True
    user.save()
    val_result = {
        'status' : Status.Success,
        'message' : None,
    }
    return render(request, 'login.html', val_result)

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
            if 'user' not in request.session:
                request.session['user'] = user_data['email_or_phone']
                return HttpResponseRedirect('home/')
    else:
        val_result = {
            'status' : Status.EmptyEmailOrPhone,
            'message' : 'Email of Phone has to be filled!',
        }

    return render(request, 'login.html', val_result)

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect('/login/')
