from dataclasses import Field, fields
import email
from email.policy import default
from enum import unique
import http
from turtle import position
from jalaliconv.utils import jalali_convertor
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib import auth
import datetime
from django.shortcuts import redirect, render
from django.db.models import F

from ipaddress import ip_address
from tempfile import template
from django.shortcuts import get_object_or_404, render
from .models import Book, Category, Comment, numbers_convertor, BookHit, Getpass, Publication
# UserProfile

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, SignuppForm, TestFormm, MyPasswordResetForm, MyForm, FinalForm, InfinityForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from star_ratings.models import UserRating

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.sessions.models import Session

from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import PasswordResetForm

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordChangeView, PasswordResetDoneView, PasswordResetView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import CommentForm
#from .forms import ProfileForm
from datetime import datetime, timedelta
from django.db.models import Count, Q
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from random import randint, randrange

from django.template.loader import render_to_string, get_template

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
import random 
from random import randrange
from .models import User
from django.db.models import Count, Q
from django.core.mail import EmailMessage
# Create your views here.
# 
# 
from django.shortcuts import render, get_object_or_404

# def post_detail(request, slug):
#     template_name = 'detail.html'
#     book = get_object_or_404(Book, slug=slug)
#     comments = book.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.book = book
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'book': book,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})
    
    
    

class BookList(ListView):
    model = Book
    
    queryset = Book.objects.filter(status='p')
    template_name = 'mybase.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        mybag = self.request.user.mybag

        # Add in a QuerySet of all the books
        context['mybag'] = mybag
        return context




 
def home(request) :
    mybag = request.user.mybag
    return render(request,'mybase2.html', {'mybag':mybag})
 
    

class DetailBooK(DetailView):
    template_name = 'detail.html'
    def get_object(self):
        slug = self.kwargs.get('slug')
        self.request.session['slug'] = slug

        book = get_object_or_404(Book, slug=slug, status="p")
        ip_address = self.request.user.ip_address
        if ip_address not in book.hits.all():
            book.hits.add(ip_address)
        return book
    
    

class CategoryList(ListView):
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects(slug=slug))
        return category.book(status='p')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return category

def categoris(request):
    context = {"category": Category.objects.filter(status=True, parent= None)}
    return render(request, 'category.html', context)

def categorychild(request, slug):
    context = {"category": Category.objects.filter(status=True, slug=slug), "catc": Category.objects.filter(status=True),"categoris": Category.objects.filter(status=True,  slug=slug), "bookis": Book.objects.all()}
    return render(request, 'categorychild.html', context)

def categoryfinal(request, slug):
    context = {"categoris": Category.objects.filter(status=True,  slug=slug), "bookis": Book.objects.all()}
    return render(request, 'categoryfinal.html', context)

def infinity(request):
    return render(request, 'infinity.html')

def request_infinity(request):
    return render(request, 'reqinfinity.html')


def categoryrecent(request):
    context = {"bookis": Book.objects.all()}
    return render(request, 'category_recent_detail.html', context)


def ghav(request):
    return render(request, 'ghav.html')



def oldcomment(request, slug, s=0):
    context = {"commits": Comment.objects.filter(active=True), "booki": Book.objects.filter(status='p', slug=slug)}
    for book in context["booki"]:
        for comment in context["commits"]:
            if comment.book == book:
                s = s + 1
    s = numbers_convertor(str(s))          
                
    context = {"commits": Comment.objects.filter(active=True), "booki": Book.objects.filter(status='p', slug=slug), "s": s}
        
    return render(request, 'oldcomment.html', context)


class Mylogin(LoginView):
     template_name = 'login2.html'
     success_url = reverse_lazy("myapp:login")
     
     





         
         
def post_detail(request, slug):
    template_name = 'newcomment.html'
    book = get_object_or_404(Book, slug=slug)
    comments = book.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.book = book
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'book': book,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})






def popular_books_detail(request):
    last_month = datetime.today()-timedelta(days=30)
    

    return render (request, 'popular_books_detail.html', {'popular_books': Book.objects.annotate(count=Count('hits'), filter=Q(bookhit__created__gt=last_month)).order_by('-count')[:5]})


def hot_books_detail(request):
    last_month = datetime.today()-timedelta(days=30)
    hot_books = Book.objects.annotate(count=Count('comments'), filter=Q(comments__created_on__gt=last_month)).order_by('-count', '-publish')[:5]
           
                            
    return render (request, 'hot_books_detail.html', {'hot_books': hot_books})




def most_stars(request):
    last_month = datetime.today()-timedelta(days=30)
    
    most_stars = Book.objects.annotate(count=Count('hits'), filter=Q(bookhit__created__gt=last_month)).order_by('-count').distinct()[:6]
                            
    return render (request, 'most_stars_detail.html', {'most_stars': most_stars})




class SearchList(ListView):
    model = Book
    template_name = 'search_list.html'
    queryset = Book.objects.filter(status='p')
    def get_queryset(self):
        search = self.request.GET.get('q')
        
        return Book.objects.filter(Q(description__icontains=search) | Q(title__icontains=search) | Q(author__icontains=search))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
    
    
    
class Mysend1(CreateView, SignupForm):
    model = User
    class_form = SignupForm()
    template_name = 'newu1.html'
    fields = ['email',]
    def myvalid(self, form):
        if self.request.method == "POST":
            form = SignupForm(self.request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = self.request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('newu1', pk=post.pk)
        else:
            form = SignupForm(self.request.POST)


    
    
class Mysend(CreateView, SignupForm):
    model = User
    class_form = SignupForm()
    template_name = 'login1.html'
    fields = ['email',]
    def myvalid(self, form):
           
        if self.request.method == "POST":
            form = SignupForm(self.request.POST)
            if form.is_valid():
                if User.objects.filter(email=email):
                    user = User.objects.filter(email=email) 
                    post = form.save(commit=False)
                    post.author = self.request.user
                    post.published_date = timezone.now()
                    post.save()
                    return redirect('login1', pk=post.pk)
        else:
             form = SignupForm(self.request.POST)



class Newu1(LoginView):
    class_form = SignupForm()
    template_name = 'newu1.html'
    
    success_url = reverse_lazy('myapp:login2')

class Login1(LoginRequiredMixin, LoginView):
    class_form = SignupForm()
    template_name = 'login1.html'
    
    success_url = reverse_lazy('myapp:login2')





def login2(request):
    passs = random.randint(1000, 9999)
    html_template = 'emailre.html'
    form = SignupForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        request.session['email'] = email

        request.session['passs'] = passs

        # pass2 = random.randint(1000, 9999)
        ctx = {
            'email': email, 'passs':passs,  'form':SignuppForm(), 'form2':SignuppForm()
        }
        message = get_template('emailre.html').render(ctx)
        msg = EmailMessage(
        ' فعالسازی حساب کاربری طاقچه',
        message,
        'm.soroushmehr@gmail.com',
        [email],
        )   
        msg.send()
        return render(request, 'login3.html', ctx)    
            
    else:
        return render(request, 'login2.html', {'form':SignuppForm(), 'passs':passs})    
    
        
        
        

def login3(request):
    form = SignuppForm(request.POST)
    email = request.session.get('email')
    passs = request.session.get('passs')
    mybag = request.user.mybag
    if form.is_valid():
        pass2 = int(form.cleaned_data['passs'])
       
        if passs == pass2:
           t= str(email)
           m = t.find('@')
           user = User.objects.get(username=t[0:m])
           user.set_password(str(passs))
           user.save()
           user = authenticate(request, username= t[0:m], password=passs)

           login(request, user)

           return render(request,'profile.html', {'email':email, 'username':t[0:m], 'myuser':t[0:m], 'mybag':mybag})

        #    if User.objects.filter(email=email):
        #     user = authenticate(request, username= t[0:m], password=passs)

            # login(request, user)
            # user.save()

        # else:  
        #        user = User.objects.create_user(email=email, username=t[0:m]+str(passs))
        #        user.password = make_password('passs')  
        #        user = auth.authenticate(username= t[0:m], password=passs)
               
        #        login(request, user)
        #        user.save()
        #        return render(request,'profile.html', {'email':email, 'username':t[0:m], 'myuser':t[0:m][len(t[0:m])-5:]})

        #     # return redirect('myapp:login4')
        #     # return HttpResponse(username)
        else:
            form = SignuppForm(request.POST)
            return render(request, 'login4.html', {'email':email, 'form': SignuppForm()})

    else:
        form = SignuppForm(request.POST)
        return render(request, 'login3.html', {'email':email, 'form': SignuppForm()})
    



# class Login4(CreateView, FinalForm):
#     model = User

def login4(request):
    form = FinalForm(request.POST)
    email = request.session.get('email')
    passs = request.session.get('passs')

    if form.is_valid():
        username = form.cleaned_data['username']
        # user = User.objects.create_user(email=email, username=username)
        # user.set_password('passs')
        # login(request, user)
        # user.save()
        # return redirect('profile')
        return HttpResponse(username)
    else:
        return HttpResponse(form.errors)

        
        
            # form = FinalForm(request.POST)
            # return render(request, 'login5.html', {'email':email, 'form': FinalForm()})
    # def get_success_url(self):
    #     user = self.request.user
    #     return reverse_lazy('profile')
 
    # def get_success_url(self):
    #     id = self.request.user.id
    #     return reverse_lazy('profile', kwargs={'id': id})  
        
    
# @login_required 
# def newu2(request):
#     # passs = random.randint(1000, 9999)
#     html_template = 'emailre.html'
#     form = SignupForm(request.POST)
#     if form.is_valid():
#         email = form.cleaned_data['email']
#         user = User.objects.create_user('m', email)
#         user.email = email
        
#         user.save()

#         request.session['passs'] = passs

#         passs = Getpass.getpp(request, email)
#         request.session['passs'] = passs

#         # pass2 = random.randint(1000, 9999)
#         ctx = {
#             'email': email, 'passs':passs,  'form':SignuppForm(), 'form2':SignuppForm()
#         }
#         message = get_template('emailre.html').render(ctx)
#         msg = EmailMessage(
#         'ایمیل فعالسازی طاقچه',
#         message,
#         'm.soroushmehr@gmail.com',
#         [email],
#         )   
#         msg.send()
#         return render(request, 'login3.html', ctx)    
            
#     else:
#         return render(request, 'login2.html', {'form':SignuppForm()})    
    

def nasb(request):
    return render(request, 'nasb.html')



class Mylogout(LogoutView):
    success_url = reverse_lazy("myapp:apii")
 
    

def buy1(request, slug):
    
    request.session['slug'] = slug

    return render(request, 'buy1.html')  
    
    
    
def buy2(request):
    email = request.session.get('email')
    slug = request.session.get('slug')
    books = Book.objects.filter(slug=slug)

    return render(request, 'buy2.html', {'email':email, 'books':books})    
    

    
    

def buy3(request):
    email = request.session.get('email')
    slug = request.session.get('slug')
    books = Book.objects.filter(slug=slug)

    form = MyForm(request.POST)
    return render(request, 'buy3.html', {'form':form, 'books':books})
        # Have Django validate the form for you
        
        
  
def buy4(request):
    form = MyForm(request.POST)  
    email = request.session.get('email')
    slug = request.session.get('slug')
    books = Book.objects.filter(slug=slug)
    username = request.session.get('username')
    passs = request.session.get('passs')
    if request.method == "POST":
        if request.user.is_authenticated: 
            if form.is_valid():
                display_type = form.cleaned_data["display_type"]
                if display_type == 'locationbox':
                    slug = request.session.get('slug')
                    books = Book.objects.filter(slug = slug)
                    list = User.mybooks(request, slug=slug)
                    ctx = {
                    'email': email, 'slug':slug,  'list':list
                    }
                    request.user.save()
                    mytime = datetime.today()
                    # request.session['msgbuy'] =msgbuy
                    message = get_template('buye1.html').render(ctx)
                    msg = EmailMessage(
                    'رسید خرید کتاب',
                    message,
                    'm.soroushmehr@gmail.com',
                    [email],
                    )   
                    msg.send()
                    # for book in books:
                    #     book.save()
                    #     buy = Buy()
                    #     buy.user = request.user
                    #     buy.position = buy.position   + 1 
                    #     buy.jtime = buy.jtime
                    #     buy.status = 'b'
                    #     buy.save()

                    #     buy.booki.add(book)
                    #     buy.status = 'a'
                    #     buy.save()
                    return render(request, 'buy5.html', ctx)    
            
    
                elif display_type == 'displaybox':
                    request.user.save()
                    # for book in books:
                    #     buy = Buy()
                    #     buy.user = request.user
                    #     buy.position = buy.position   + 1 
                    #     buy.jtime = buy.jtime
                    #     buy.status = 'b'
                    #     buy.save()

                    #     buy.booki.add(book)
                    #     buy.status = 'b'
                    #     buy.save()
                    # request.session['msgbuy'] =msgbuy
                    
                    mytime = datetime.today()
   
                    ctx = {
                      'email': email
                     }
                    message = get_template('buye2.html').render(ctx)
                    msg = EmailMessage(
                     'لغو خرید کتاب',
                    message,
                     'm.soroushmehr@gmail.com',
                     [email],
                     )   
                    msg.send()
                    request.session['email'] = email
                    # request.session['msgbuy'] = msgbuy
    
                    return render(request, 'buy6.html')    
                
                 
            return HttpResponse('لطفا به عقب برگردید و یکی از گزینه ها را انتخاب کنید')

      
  
        
    
class Profile(UpdateView):
    model = User    
    template_name = 'profile.html'
    fields = ['email',]

    success_url = reverse_lazy('profile')

    
    def get_object(self):
        email = self.request.session.get('email')
        # timebuy = self.request.session.get('timebuy')

        username = self.request.session.get('username')
        self.request.username = username
        self.request.email = email
        self.request.user.save()
        self.is_authenticated = True
        return User.objects.get(pk=self.request.user.pk)
    
            
          
  
def mybooks(request):
    slug = request.session.get('slug')
    books = Book.objects.filter(slug=slug)
    username = request.session.get('username')
    email = request.session.get('email')
    passs = request.session.get('passs')
    mytime = request.session.get('mytime')
    msgbuy = request.session.get('msgbuy')
    if request.user.is_authenticated: 
        list = User.mybooks(request, slug=slug)
        i = range(0, len(list))
        list1 = []
        list2= []
            
        for j in i:
            list1.append(list[j][0])
            list2.append(list[j][1])
        request.session['list1'] = list1
        request.session['list2'] = list2
        
        email = request.session.get('email')
        msgby = request.session.get('msgbuy')
 
        return render(request, 'mybooks.html',  {'email':email, 'books':books, 'list1':list1, 'list2':list2, 'i':i})

    



    
# def buyhistory(request):
#     # slug = request.session.get('slug')
#     # books =Book.objects.filter(slug=slug)
#     email = request.session.get('email')
#     buys = Buy.objects.all().distinct()
#     n = buys.count()
#     num = range(0,n+1)
#     books = Book.objects.all()
#     users = User.objects.all()
#     for buy in buys:
#         return HttpResponse(buy.jtime)
    
#     # return render(request, 'buyhistory.html',  {'email':email, 'buys':buys, 'books':books, 'users':users})

    
#     # # user = User.objects.get(pk=request.user.pk)
    
#     # slug = request.session.get('slug')
#     # books = Book.objects.filter(slug=slug)
    
#     # username = request.session.get('username')
#     # passs = request.session.get('passs')
#     # if request.user.is_authenticated and request.user.email == email: 
#     #     # user.set_password(str(passs))

#     #     # s = UserProfile(created=datetime.today(), mybag='0')
#     #     # s.save()
#     #     # for book in books:
#     #     #    book.save()
#     #     #    s.mybooks.add(book)

        
#     #     # mybooks = s.mybooks
#     #     email = request.session.get('email')
#     #     msgby = request.session.get('msgbuy')
#     # # book.title = request.session.get('book.title')
#     #     timebuy = request.session.get('timebuy')
    
        
        

   
def manageq(request):
    return render(request, 'manageq.html')


def karnameh(request):
    return render(request, 'karnameh.html')
   
    
def publications(request):
    
    publications = Publication.objects.all.distinct()[:6]
    books =  Book.objects.all.distinct()[:6]
                      
    return render (request, 'mdetail.html', {'publications': publications, 'books':books})





def pretebar(request):
    email = request.session.get('email')
    mybag = request.user.mybag

    # request.session['mybag'] = mybag
    form = InfinityForm(request.POST)
    return render(request, 'pretebar.html', {'form':form, 'mybag':mybag})



def etebar(request):

    mybag = request.user.mybag
    email = request.session.get('email')
   # user = User.objects.get(pk=request.user.pk)
    form = InfinityForm(request.POST)  

        
    
    if request.method == "POST":
        if request.user.is_authenticated: 

        # user.set_password(str(passs))
        #    s = UserProfile(created=datetime.today(), mybag='0')
        #    s.save()

           if form.is_valid():
               infinity_type = form.cleaned_data["infinity_type"]


               if infinity_type == '1':
                   mybag += 100000

               elif infinity_type == '2':

                   mybag = mybag + 200000


               elif infinity_type == '3':
                   mybag += 500000
               
               request.user.mybag = mybag
               request.user.save()
            #    mybag = request.user.mybags
            #    request.user.mybags = mybag
            #    request.user.save()            
               ctx = {'mybag':mybag }
               return render(request, 'etebar.html', ctx)    

           else:
                return HttpResponse('لطفا به عقب برگردید و یکی از گزینه ها را انتخاب کنید')






def detailbuy(request, slug):
    books = Book.objects.filter(slug=slug)
    ctx = {'books':books}
    return render(request, 'detailbuy.html', ctx)
    
    
    
    
    
    
def eshtbi(request):
    ctx = {
        'weak': 'یک هفته',
        'pweak':'۱۵۰۰۰تومان', 'onemonth': 'یک ماه', 'ponemonth':'۳۰۰۰۰تومان', 
         'threemonth':'سه ماه', 'pthreemonth': '۶۵۰۰۰تومان', 'sixmonth':'شش ماه', 'psixmonth':'۱۲۰۰۰۰تومان', 'oneyear':'یک سال', 'poneyear':'۲۰۰۰۰۰تومان'
    }
    return render(request, 'eshtbi.html', ctx)   




def subscribe(request, slug):
    pay = 'p'+ slug
    x = slug
    request.session['x'] = x

    ctx = {
        'weak': 'یک هفته',
        'pweak':'۱۵۰۰۰تومان', 'onemonth': 'یک ماه', 'ponemonth':'۳۰۰۰۰تومان', 
         'threemonth':'سه ماه', 'pthreemonth': '۶۵۰۰۰تومان', 'sixmonth':'شش ماه', 'psixmonth':'۱۲۰۰۰۰تومان', 'oneyear':'یک سال', 'poneyear':'۲۰۰۰۰۰تومان'}
    t = ctx[pay]
    d = ctx[slug]

    mybag = request.user.mybag
    ctx = {
        'weak': 'یک هفته',
        'pweak':'۱۵۰۰۰تومان', 'onemonth': 'یک ماه', 'ponemonth':'۳۰۰۰۰تومان', 
         'threemonth':'سه ماه', 'pthreemonth': '۶۵۰۰۰تومان', 'sixmonth':'شش ماه', 'psixmonth':'۱۲۰۰۰۰تومان', 'oneyear':'یک سال', 'poneyear':'۲۰۰۰۰۰تومان', 'pay':t, 'd':d, 'mybag':mybag}


    request.session['d'] = d
    request.session['t'] = t
    request.session['x'] = x
    ctxt = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'',  'mybag':mybag}

    tpay = ctxt[pay]
    dday = ctxt[slug]
    
    # buy = Buy()
    # buy.user = request.user
    # buy.timebuy  = datetime.today()
    # buy.status = 'b'
    # buy.msgbuy = slug
    # buy.position = buy.positions + 1
    
    # buy.save()
    

    ctx = {
        'weak': 'یک هفته',
        'pweak':'۱۵۰۰۰تومان', 'onemonth': 'یک ماه', 'ponemonth':'۳۰۰۰۰تومان', 
         'threemonth':'سه ماه', 'pthreemonth': '۶۵۰۰۰تومان', 'sixmonth':'شش ماه', 'psixmonth':'۱۲۰۰۰۰تومان', 'oneyear':'یک سال', 'poneyear':'۲۰۰۰۰۰تومان', 'pay':t, 'd':d, 'mybag':mybag, 'tpay':tpay}

    
    return render(request, 'subscribe.html', ctx)
    




def buysubag(request):
    mybag = request.user.mybag
    x = request.session.get('x') 
    ctx = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'',  'mybag':mybag}
    pay = 'p' + x
    tpay = ctx[pay]
    dday = ctx[x]

    ctx = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'',  'mybag':mybag, 'pay':tpay, 'x':dday}
    
    request.session['tpay'] = tpay
    request.session['dday'] = dday

    mybag = mybag - int(tpay)
    request.user.mybag = mybag 
    request.user.save()
    
    request.user.special_user = timedelta(days=int(dday)) +  datetime.today()
    mytime = request.user.special_user
    request.user.save()
    ctx = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'',  'mybag':mybag, 'pay':tpay, 'days':dday, 'mytime':mytime}

    return render(request, 'buysubag.html', ctx) 




def buysub(request):
    
    x = request.session.get('x') 
    ctx = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'2000000'}
    pay = 'p' + x
    tpay = ctx[pay]
    dday = ctx[x]

    ctx = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'2000000', 'pay':tpay, 'x':dday}
    
    request.session['tpay'] = tpay
    request.session['dday'] = dday

    
    request.user.special_user = timedelta(days=int(dday)) +  datetime.today()
    mytime = request.user.special_user
    request.user.save()
    ctx = {
        'weak': '7 ',
        'pweak':'150000', 'onemonth': '30 ', 'ponemonth':'300000', 
         'threemonth':'90 ', 'pthreemonth': '650000', 'sixmonth':'180 ', 'psixmonth':'1200000', 'oneyear':'365 ', 'poneyear':'2000000', 'pay':tpay, 'days':dday, 'mytime':mytime}

    return render(request, 'buysub.html', ctx) 




    