from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from users.forms import RegisterForm


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:verify-email')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        #send verification code
        return redirect(self.success_url)

    def form_invalid(self, form):
        pass




def verify_email(request):
    pass


class LoginView(TemplateView):
    template_name = 'users/login.html'


class WishlistView(TemplateView):
    template_name = 'users/wishlist.html'

class CartView(TemplateView):
    template_name = 'users/cart.html'

class ChangePassword(TemplateView):
    template_name = 'users/reset-password.html'


class AccountView(TemplateView):
    template_name = 'users/acount.html'
class CheckoutView(TemplateView):
    template_name = 'products/checkout.html'