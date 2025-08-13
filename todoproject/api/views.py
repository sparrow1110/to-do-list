from django.http import Http404
from django.middleware.csrf import get_token
from rest_framework import status, generics, serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import TaskSerializer
from todo.models import Task


class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user__id=self.request.user.id)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {
            'tasks': response.data,
            'csrf_token': get_token(request)
        }
        return response

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response({
                'success': True,
                'message': 'Задача успешно добавлена!',
                'data': serializer.data,
            })
        except serializers.ValidationError as e:
            return Response({
                'success': False,
                'message': serializer.errors['name'][0]
            }, status=status.HTTP_400_BAD_REQUEST)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']

    def get_queryset(self):
        return Task.objects.filter(user__id=self.request.user.id)

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise NotFound({
                'success': False,
                'message': 'Задача не найдена'
            })

    def partial_update(self, request, *args, **kwargs):
        change = request.data.get("change")
        if not change:
            return Response({
                'success': False,
                'message': 'Необходим параметр change',
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            if abs(int(change)) != 1:
                raise ValueError
            instance = self.get_object()
            instance.is_completed += int(change)
            instance.save()
            return Response({
                'success': True,
                'message': 'Статус задачи изменен!',
                'data': self.get_serializer(instance).data,
            })
        except ValueError:
            return Response({
                'success': False,
                'message': 'Параметр change должен быть числом 1 или -1',
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'message': 'Задача успешно удалена!',
        })

