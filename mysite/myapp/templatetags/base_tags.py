from ..models import Category, Book
from django import template
from datetime import datetime, timedelta
from django.db.models import Count, Q
from star_ratings.models import UserRating


register = template.Library()

@register.inclusion_tag('categoris.html')
def category_page():
    context = {"category": Category.objects.published(status=True, parent= None), "catpa": Category.objects.published(status=True, cat_has_parent=True)}
    return context


@register.inclusion_tag('popular_books.html')
def popular_books():
    last_month = datetime.today()-timedelta(days=30)

    return {'popular_books': Book.objects.annotate(count=Count('hits'), filter=Q(bookhit__created__gt=last_month)).order_by('-count').distinct()}


@register.inclusion_tag('hot_books.html')
def hot_books():
    last_month = datetime.today()-timedelta(days=30)
    return {'hot_books': Book.objects.distinct().annotate(count=Count('comments'), filter=Q(comments__created_on__gt=last_month)).order_by('-count').distinct(), 'hot_books6':  Book.objects.distinct().annotate(count=Count('comments'), filter=Q(comments__created_on__gt=last_month)).order_by('-count').distinct()[:6]}


# @register.inclusion_tag('category_recent.html')
# def categor_recent():
#     last_month = datetime.today()-timedelta(days=30)

#     return {'catrec_books': Book.objects.annotate(filter=Q(publish__created__gte=last_month)).order_by('-publish')}


# porbazdid
@register.inclusion_tag('most_stars.html')
def most_stars():
    last_month = datetime.today()-timedelta(days=30)
    return {'most_stars':Book.objects.annotate(count=Count('hits'), filter=Q(bookhit__created__gt=last_month)).order_by('-count').distinct()[:6]}
