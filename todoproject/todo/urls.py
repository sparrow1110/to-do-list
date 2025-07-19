from django.urls import path
from . import views


urlpatterns = [
    path("", views.TaskListView.as_view(), name='home'),
    path("add/", views.AddTaskView.as_view(), name='add'),
    path("update/<int:task_id>", views.UpdateTask.as_view(), name='update'),
    path("delete/<int:task_id>", views.DeleteTask.as_view(), name='delete')
]