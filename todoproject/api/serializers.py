from rest_framework import serializers

from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "is_completed", )

    def validate_name(self, value):
        if len(value) == 0:
            raise serializers.ValidationError("Название не может быть пустым")
        if len(value) > 100:
            raise serializers.ValidationError("Длина превышает 100 символов")
        return value
