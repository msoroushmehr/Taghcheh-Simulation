from django.contrib import admin
from django.urls import path, include
from .views import BookList, DetailBooK, Mylogout, buysubag, categoris, categorychild, Mylogin, ghav, categoryfinal, infinity, mybooks, request_infinity, oldcomment, post_detail, popular_books_detail, hot_books_detail, SearchList, categoryrecent, Mysend, Login1, login2, login3,  Newu1, Mysend1, nasb, home, buy1, buy2, buy3, buy4, login4,  manageq, karnameh, detailbuy, pretebar,etebar, eshtbi, subscribe, buysub
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordChangeView, PasswordResetDoneView, PasswordResetView
from django.urls import reverse

app_name = 'myapp'

urlpatterns = [path('', BookList.as_view(), name='api'), 
path('', home, name='apii'),              

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
path('popularbooksdetail/', popular_books_detail, name='popular_books_detail' ),
path('mysend', Mysend.as_view(), name='mysend' ),
path('hotbooksdetail/', hot_books_detail, name='hot_books_detail' ),
path('search/', SearchList.as_view(), name='search'), 
path('book/pc', categoryrecent , name='categoryrecent'),
# path('login1/', Login1.as_view(), name='login1' ),
path('login2/', login2, name='login2' ),
path('login3/', login3, name='login3' ),
path('login4/', login4, name='login4' ),

path('newu1/', Newu1.as_view(), name='newu1' ),
path('mysend1', Mysend1.as_view(), name='mysend1' ),
path('install', nasb, name='nasb' ),
path('logout', Mylogout.as_view(), name='mylogout' ),
path('install', nasb, name='nasb' ),
path('sale/<slug:slug>', buy1, name='buy1' ),
path('sale2', buy2, name='buy2' ),
path('sale3', buy3, name='buy3' ),
path('sale4', buy4, name='buy4' ),
path('mybooks', mybooks, name='mybooks' ),
# path('buyhistory', buyhistory, name='buyhistory' ),
path('manageq', manageq, name='manageq' ),
path('readingreport', karnameh, name='karnameh' ),
path('detailbuy/<slug:slug>', detailbuy, name='detailbuy'),
path('pretebar', pretebar, name='pretebar' ),
path('etebar', etebar, name='etebar' ),
path('eshtbi', eshtbi, name='eshtbi' ),
path('subscribe/<slug:slug>', subscribe, name='subscribe'),
path('buysubag', buysubag, name='buysubag'),
path('buysub', buysub, name='buysub'),

]         