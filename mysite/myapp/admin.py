from django.contrib import admin
from .models import Book, Publication


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'slug', 'publish')
    search_fields = ('title', 'description')
    prepulated_fields = {'slug':('title',)}
    ordering = ('status', 'publish')
admin.site.register(Book, BookAdmin)
# Register your models here.

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Publication, PublicationAdmin)