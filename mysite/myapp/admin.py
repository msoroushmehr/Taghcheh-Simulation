from tabnanny import verbose
from telnetlib import IP
from unicodedata import category
from django.contrib import admin
from .models import Book, MyIPAddress, Publication, Category
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import  Comment, MyIPAddress


verbose_name = "طاقچه"




class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

admin.site.register(Publication, PublicationAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent' )
    list_filter = (['status'])
    search_fields = ('title',)
    ordering = ('-parent__', )
    

admin.site.register(Category, CategoryAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'slug', 'publish', 'publication', 'category_to_str', 'author', 'price')
    search_fields = ('title', 'description')
    prepulated_fields = {'slug':('title',)}
    ordering = ('status', 'publish')
    
    
admin.site.register(Book, BookAdmin)


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('special_user', 'is_special_user')

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'mybags']

   
admin.site.register(User, UserAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'book' , 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment, CommentAdmin)



class MyIPAddressAdmin(admin.ModelAdmin):
    list_display =('ip_address', 'name' )  
    
admin.site.register(MyIPAddress, MyIPAddressAdmin)






    
    
    