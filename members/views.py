from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def emailsignup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        User.objects.create_user(email, password)
        messages.success(request, 'Account created!')
    return render(request, "emailsignup.html")



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'test' and password == 'password123':
            return HttpResponse("Ви успішно увійшли!")
        else:
            return HttpResponse("Невірний логін або пароль!")
    return render(request, 'login.html')


