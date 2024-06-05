from lib2to3.fixes.fix_input import context

from django import template

from products.models import ProductModel

register = template.Library()


@register.filter
def get_user_cart(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(pk__in=cart)
    return products


@register.filter
def in_cart(product, request):
    return product.pk in request.session.get('cart', [])


@register.filter
def get_likes(request):
    likes = request.session.get('likes', [])
    products = ProductModel.objects.filter(pk__in=likes)
    return products


@register.filter
def get_likes_in(product_like, request):
    return product_like.pk in request.session.get('likes', [])