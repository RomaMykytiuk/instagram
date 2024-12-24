from django.urls import path
from . import views


urlpatterns = [
    path('members/', views.members, name='members'),
    path('accounts/emailsingup/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.edit_profile, name='profile'),
]



