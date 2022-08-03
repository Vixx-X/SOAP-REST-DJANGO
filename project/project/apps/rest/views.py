from rest_framework import viewsets

from .serializers import TaskSerializer
from project.apps.todo.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for tasks
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
