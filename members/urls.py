from django.urls import path
from . import views


urlpatterns = [
   path('members/', views.members, name='members'),
   path('login/', views.login_view, name='login'),
   path("accounts/emailsingup/" ,views.register, name="register"),
  # path('profile/', profile_view, name='profile'),

]



