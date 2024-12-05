from django.urls import path
from . import views
from .views import profile_view


urlpatterns = [
   path('members/', views.members, name='members'),
   path('login/', views.login_view, name='login'),
   path("accounts/emailsingup/" ,views.emailsignup, name="emailsingup"),
   path('profile/', profile_view, name='profile'),

]



