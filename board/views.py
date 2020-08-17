from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

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
