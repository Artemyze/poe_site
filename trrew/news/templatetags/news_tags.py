from django import template
from news.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
	return Category.objects.all()


@register.inclusion_tag('news/_sidebar1.html')
def def_list_categories():
	return {'category': get_categories}

