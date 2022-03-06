from turtle import update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Book(models.Model):
    STATUS_CHOICES = [('d', 'draft'), ('p', 'publish')]
    title = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    description = models.TextField()
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to="Images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    
    