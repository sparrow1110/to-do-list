from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),
    path("users/", include("users.urls", namespace="users")),
    path("", include("api.urls")),
]

handler404 = 'todo.views.page_not_found'