from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    class Status(models.IntegerChoices):
        NOT_STARTED = 0, 'Не начато'
        IN_PROCESS = 1, 'В процессе'
        FINISHED = 2, 'Завершено'

    name = models.CharField(max_length=100, blank=True)
    is_completed = models.IntegerField(choices=Status.choices, default=Status.NOT_STARTED)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None, related_name="tasks")

    class Meta:
        ordering = ["-pk"]