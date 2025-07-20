from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

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
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            task_html = render_to_string('todo/task_item.html', {'todo': task}, request=self.request)
            return JsonResponse({
                'success': True,
                'message': 'Задача успешно добавлена!',
                'task_html': task_html,
                'csrf_token': get_token(self.request)  # Возвращаем новый CSRF-токен
            })
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': 'Ошибка: ' + str(form.errors.as_text()),
                'csrf_token': get_token(self.request)  # Возвращаем новый CSRF-токен
            })
        return super().form_invalid(form)

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
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            task_html = render_to_string('todo/task_item.html', {'todo': task}, request=self.request)
            return JsonResponse({
                'success': True,
                'message': 'Статус задачи изменен!',
                'task_html': task_html,
                'csrf_token': get_token(self.request)  # Возвращаем новый CSRF-токен
            })
        return redirect('home')


class DeleteTask(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return redirect('home')

    def post(self, request, task_id):
        task = Task.objects.filter(pk=task_id, user_id=self.request.user.id)
        if task.exists():
            task.delete()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Задача успешно удалена!',
                    'csrf_token': get_token(self.request)  # Возвращаем новый CSRF-токен
                })
        return redirect('home')


def page_not_found(request, exception):
    return render(request, "todo/page404.html", status=404)