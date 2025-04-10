from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('accounts/emailsingup/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/',views.user_logout, name='logout'),
    path('profile/', views.show_profile, name='profile'),
    path('home/', views.home_view, name='home'),
    path('search/', views.search_view, name='search'),
    path('create_post/', views.create_post, name='create_post'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]



