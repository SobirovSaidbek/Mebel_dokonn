from lib2to3.fixes.fix_input import context

from django import template

from products.models import ProductModel

register = template.Library()


@register.filter
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(pk__in=cart)
    return products



@register.simple_tag(takes_context=True)
def in_cart(request, pk):
    request = context['request']
    cart = request.session.get('cart', [])
    return pk in cart