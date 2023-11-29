from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from clgweb.models import Subscription
# Create your views here.


def home(request):
    return render(request, "index.html")


def subscribe(request):
    email = request.GET.get('email', False)
    Subscription.objects.create(email=email)
    message = 'you have successfully subscribed'

    return JsonResponse({'message': message})


def about(request):
    return render(request, "about.html")


def pylang(request):
    return render(request, 'pylang.html')


def pythonsoftware(request):
    return render(request, 'python software.html')


def javasoftware(request):
    return render(request, 'java software.html')


def csoftware(request):
    return render(request, 'c software.html')


def advancecsoftware(request):
    return render(request, 'advancec software.html')


def pythonide(request):
    return render(request, 'python ide.html')


def log_in(request):
    return render(request, 'login.html', {'msg': 'Hi'})


def contact(request):
    return render(request, 'contact.html')


def process_login(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    print(username, password)

    user = authenticate(request, username=username, password=password)
    print(user)
    if user is not None:

        if user.is_active:
            login(request, user)
            #message = 'You are successfully logged in'
            return redirect('/home')
    else:
        message = 'Your are not Authorized.'
        messages.warning(request, message)
    # return HttpResponse(message)
    return redirect('/login')


def process_logout(request):
    logout(request)
    return redirect('/home')
    # return HttpResponse('you r Logged out')
