from turtle import update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html

class User(AbstractUser):
    pass


class Publication(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

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
    publication = models.ForeignKey(Publication, null=True, on_delete=models.CASCADE)
    def image_tag(self):
        return format_html("<img width=100 height=75 src='{}'>".format(self.image.url))
    
    def __str__(self):
        return self.title
   
   
   
