from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from project.apps.todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Task serializer
    """

    class Meta:
        model = Task
        fields = "__all__"
