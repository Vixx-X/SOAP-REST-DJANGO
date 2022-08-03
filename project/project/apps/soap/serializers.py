from project.apps.todo.models import Task as TaskModel
from spyne.util.django import DjangoComplexModel


class Task(DjangoComplexModel):
    class Attributes(DjangoComplexModel.Attributes):
        django_model = TaskModel
