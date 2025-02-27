from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import UserRegistrationForm,LoginForm,PostForm
from .models import Post,User,Image
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
            return redirect('profile')
        else: messages.error(request,"Помилка")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def show_profile(request):
    user = request.user
    return render(request, 'profile.html',{'user': user})




def home_view(request):
    posts = [
        {
            'username': 'Григорій',
            'likes': 152,
            'caption': 'Природа України!😍'
        },
        {
            'username': 'Данило',
            'likes': 1756,
            'caption': 'Я найкращий вчитель Романа!'
        }
        # Додайте більше постів тут
    ]
    return render(request, 'home.html', {'posts': posts})




def create_post_view(request):
    if request.method == 'POST':
        # Логіка для створення поста
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Збережіть пост у вашій базі даних
        ...
        return redirect('home')
    context = {}
    return render(request, 'create_post.html', context)



def search_view(request):
    # Логіка для пошуку
    query = request.GET.get('q')
    results = []
    if query:
        # Виконайте пошук у вашій базі даних або іншому джерелі даних
        results = ...  # Замість цього додайте вашу логіку пошуку
    context = {'results': results, 'query': query}
    return render(request, 'search.html', context)

from django.shortcuts import render

def notifications_view(request):
    # Логіка для відображення сповіщень
    notifications = [
        'Notification 1',
        'Notification 2',
        'Notification 3',
    ]
    context = {'notifications': notifications}
    return render(request, 'notifications.html', context)


# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'create_post.html'
#     success_url = reverse_lazy('create_post')
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.author = self.request.user
#         post.save()
#
#         files = form.cleaned_data.get('images')
#
#
#         for f in files:
#             Image.objects.create(post=self.object, image=f)
#         return super().form_valid(form)
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))

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
