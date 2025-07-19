from django import forms
from django.core.exceptions import ValidationError

from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите название задачи...',
        })
    )

    class Meta:
        model = Task
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 100:
            raise ValidationError('Длина превышает 100 символов')
        elif len(name) == 0:
            raise ValidationError('Название не может быть пустым')

        return name
