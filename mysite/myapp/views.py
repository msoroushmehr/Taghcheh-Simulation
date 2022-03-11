from django.shortcuts import get_object_or_404, render
from .models import Book, Category, Comment, numbers_convertor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import CommentForm
#from .forms import ProfileForm



from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
from .models import User
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
    template_name = 'home.html'
    

class DetailBooK(DetailView):
    template_name = 'detail.html'
    def get_object(self):
        slug = self.kwargs.get('slug')
        book =  get_object_or_404(Book, slug=slug, status="p")
        
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
     template_name = 'login.html'
     

         
         
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




