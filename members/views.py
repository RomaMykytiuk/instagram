from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def emailsignup(request):
    return HttpResponse(loader.get_template('emailsignup.html').render())

#views.py


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        User.objects.create_user(username, password)
        messages.success(request, 'Account created!')
        # return redirect("user_page")
    return render(request, "register.html")




