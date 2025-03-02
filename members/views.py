from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm, LoginForm, PostForm
from .models import Post, User, Image
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request, "Ви успішно Увійшли!")
            return redirect('profile')
        else: messages.error(request, "Помилка")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def show_profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def home_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(caption__icontains=query)
    context = {'results': results, 'query': query}
    return render(request, 'search.html', context)

def notifications_view(request):
    notifications = [
        'Notification 1',
        'Notification 2',
        'Notification 3',
    ]
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            images = request.FILES.getlist('images')
            for img in images:
                Image.objects.create(post=post, image=img)

            return redirect('home')
        else:
            return render(request, 'create_post.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
