from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm




from .models import User

def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def emailsignup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        full_name = request.POST.get('full_name')
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        User.objects.create(email=email, password=make_password(password),full_name=full_name)
        messages.success(request, 'Account created!')
        return redirect('login')
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




def profile_view(request):
    # Отримати перший профіль із бази або створити новий
    profile, created = Profile.objects.get_or_create(id=1)

    if request.method == 'POST':
        # Передати існуючий профіль у форму
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # Зберегти зміни
            return redirect('profile')  # Перенаправлення на ту ж сторінку
    else:
        # Завантажити форму з існуючими даними профілю
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})
