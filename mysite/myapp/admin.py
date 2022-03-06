from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    search_fields = ('title', 'description')
    prepulated_fields = {'slug':('title',)}
    ordering = ('status', 'publish')
admin.site.register(Book, BookAdmin)
# Register your models here.
