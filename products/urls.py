from django.urls import path

from products.views import ProductsListView, ProductDetailView, add_or_remove

app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('cart/<int:pk>/', add_or_remove, name='add-or-remove'),
    path('', ProductsListView.as_view(), name='list'),
]