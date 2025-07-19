from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path("register/", views.RegisterUser.as_view(), name='register'),
    path("login/", views.LoginUser.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout')
]