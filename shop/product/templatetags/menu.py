from django.template import Library
from ..models import Category


register = Library()


@register.inclusion_tag("menu.html") # menu in navbar
def menu():
    category = Category.objects.all()
    return {'category': category}
