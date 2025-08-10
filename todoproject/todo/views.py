from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class TaskView(LoginRequiredMixin, TemplateView):
    template_name = 'todo/index.html'
    login_url = 'users:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


def page_not_found(request, exception):
    return render(request, "todo/page404.html", status=404)