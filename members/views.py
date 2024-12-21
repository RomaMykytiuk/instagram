from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import login


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')
        else:
            messages.error(request, "Помилка!")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')  # Додаємо цю змінну
#
#         if username == 'test' and password == 'password123':
#             return HttpResponse("Ви успішно увійшли!")
#         else:
#             return HttpResponse("Невірний логін або пароль!")
#     return render(request, 'login.html')

# def profile_view(request):
#     profile, created = Profile.objects.get_or_create(id=1)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=profile)
#
#     return render(request, 'profile.html', {'form': form, 'profile': profile})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request,"Ви успішно Увійшли!")
            return redirect("members")
        else: messages.error(request,"Помилка")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
