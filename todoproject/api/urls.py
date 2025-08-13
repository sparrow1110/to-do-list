from django.urls import path
from . import views


urlpatterns = [
    path("api/v1/tasks/<int:pk>/", views.TaskRetrieveUpdateDestroyAPIView.as_view()),
    path("api/v1/tasks/", views.TaskListCreateAPIView.as_view()),
]