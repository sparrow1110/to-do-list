from django.urls import path
from . import views


urlpatterns = [
    path("api/v1/tasks/<int:task_id>/", views.TaskAPIView.as_view()),
    path("api/v1/tasks/", views.TaskAPIView.as_view()),
]