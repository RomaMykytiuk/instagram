import random
from django.core.management.base import BaseCommand
from  ..models import User, Post, Like, Tag, Image, PostTag
from django.utils import timezone
from faker import Faker
fake = Faker()

class Command(BaseCommand):
    help = 'заповнює базу даних тестовими даними'