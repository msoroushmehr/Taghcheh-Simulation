from ..models import Category
from django import template

register = template.Library()

@register.inclusion_tag('categoris.html')
def category_page():
    context = {"category": Category.objects.published(status=True, parent= None), "catpa": Category.objects.published(status=True, cat_has_parent=True)}
    return context