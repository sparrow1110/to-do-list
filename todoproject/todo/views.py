from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView

from .models import Task
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'
    login_url = 'users:login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['form'] = TaskForm()
        return context

    def get_queryset(self):
        return Task.objects.filter(user_id=self.request.user.id)


class AddTaskView(LoginRequiredMixin, FormView):
    form_class = TaskForm
    template_name = 'todo/index.html'
    success_url = reverse_lazy('home')
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['todo_list'] = Task.objects.filter(user_id=self.request.user.id)
        return context

    def form_valid(self, form):
        w = form.save(commit=False)
        w.user = self.request.user
        w.save()
        messages.success(self.request, "Задача успешно добавлена!")
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return redirect('home')


class UpdateTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return redirect('home')

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id, user_id=request.user.id)
        change = int(request.POST.get('change', 0))
        task.is_completed = task.is_completed + change
        task.save()
        messages.success(request, "Статус задачи изменен")
        return redirect('home')


class DeleteTask(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return redirect('home')

    def post(self, request, task_id):
        t = Task.objects.filter(pk=task_id, user_id=self.request.user.id).delete()
        if t:
            messages.success(request, "Задача успешно удалена!")
        return redirect('home')


def page_not_found(request, exception):
    return render(request, "todo/page404.html", status=404)


def handler500(request, exception=None):
    return render(request, "todo/page500.html", status=500)
