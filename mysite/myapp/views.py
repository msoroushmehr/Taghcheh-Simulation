from django.shortcuts import render
from .models import Book
# Create your views here.
def api(request):
    context = {'book':Book.objects.filter(status="p").order_by("-publish")[:6]}
    return render(request, 'home.html', context)