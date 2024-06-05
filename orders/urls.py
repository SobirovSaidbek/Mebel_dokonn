from django.urls import path

from orders.views import CheckoutView, OrderView

app_name = 'orders'

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order/', OrderView.as_view(), name='order')
]