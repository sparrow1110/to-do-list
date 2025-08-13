from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=100,
        error_messages={
            'blank': "Название не может быть пустым!",
            'max_length': "Длина названия превышает 100 символов!",
        }
    )

    class Meta:
        model = Task
        fields = ("id", "name", "is_completed", )
