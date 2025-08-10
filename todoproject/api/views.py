from django.middleware.csrf import get_token
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import TaskSerializer
from todo.models import Task


class TaskAPIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get("task_id")

        if task_id:
            try:
                task = Task.objects.get(pk=task_id, user=request.user)
                return Response({
                    'task': TaskSerializer(task).data,
                })
            except Task.DoesNotExist:
                return Response({
                    'success': False,
                    'message': 'Задача не найдена'
                }, status=status.HTTP_404_NOT_FOUND)

        tasks = Task.objects.filter(user=request.user)
        return Response({
            'tasks': TaskSerializer(tasks, many=True).data,
            'csrf_token': get_token(request)
        })

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'success': False,
                'message': serializer.errors['name'][0]
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=request.user)
        return Response({
            'success': True,
            'message': 'Задача успешно добавлена!',
            'data': serializer.data,
        })

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get("task_id", None)
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Задача не найдена',
            }, status=status.HTTP_404_NOT_FOUND)

        change = request.data.get("change")
        if not change:
            return Response({
                'success': False,
                'message': 'Необходим параметр change',
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            if abs(int(change)) != 1:
                raise ValueError
            task.is_completed += int(change)
            task.save()
            return Response({
                'success': True,
                'message': 'Статус задачи изменен!',
                'data': TaskSerializer(task).data,
            })
        except ValueError:
            return Response({
                'success': False,
                'message': 'Параметр change должен быть числом 1 или -1',
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("task_id", None)
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({
                'success': False,
                'message': 'Задача не найдена',
            }, status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response({
            'success': True,
            'message': 'Задача успешно удалена!',
        })

