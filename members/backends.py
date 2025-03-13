# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import BaseBackend
# from django.conf import settings
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
#
#
#
# class EmailOrUsernameModelBackend(ModelBackend):
#
#     def authenticate(self, request, username=None, password=None):
#         login_valid = (settings.ADMIN_LOGIN == username)
#         pwn_valid = check_password(password ,settings.ADMIN_PASSWORD)
#         if login_valid and pwn_valid:
#             try:
#                 user = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 user = User(username=username)
#                 user.is_staff = True
#                 user.is_superuser = True
#                 user.save()
#             return user
#         return None
#     def get_user(self,user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
#
#
#
#
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if not username:
            return None
        try:
            if "@" in username:
                user = UserModel.objects.get(email=username)
            else:
                user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
