from django.contrib import admin
from django.urls import path
from .views import BookList, DetailBooK, categoris, categorychild, Mylogin, ghav, categoryfinal, infinity, request_infinity, oldcomment, post_detail
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [path('', BookList.as_view(), name='api'), 
path('book/<slug:slug>', DetailBooK.as_view(), name='detail'),
path('categories', categoris, name='categoris'),   
path('categories/<slug:slug>', categorychild, name='categorychild'), 
path('categoriesfinal/<slug:slug>', categoryfinal, name='categoryfinal'),   
path('login/', Mylogin.as_view(), name='login' ),
path('ghav', ghav, name='ghav' ),
path('infinity/', infinity, name='infinity' ),
path('reinfinity/', request_infinity, name='reinfinity' ),
path('book/oldcomment/<slug:slug>', oldcomment, name='old_comment' ),
path('book/newcomment/<slug:slug>', post_detail, name='new_comment' ),


]            