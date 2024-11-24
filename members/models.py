from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True)
    password = models.CharField(max_length=100,)

class Post(models.Model):
    author = models.ForeignKey("User", on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    caption = models.CharField(max_length=500)


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_id = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Image(models.Model):
    image = models.ImageField(upload_to='posts/')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="images")


class PostTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="post_tags")
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name="post_tags")