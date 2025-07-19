from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages

from users.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}
    redirect_authenticated_user = True


class RegisterUser(UserPassesTestMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.info(self.request, "Вы уже авторизованы!")
        return redirect('home')
