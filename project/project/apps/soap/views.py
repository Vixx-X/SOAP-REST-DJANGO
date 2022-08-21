from django.db.utils import IntegrityError

from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoService

from project.apps.todo.models import Task as TaskModel

from .serializers import Task


class TaskService(DjangoService):
    """
    Service for tasks handling
    """

    @rpc(Integer, Integer, _returns=Iterable(Task))
    def list_task(ctx, limit, offset):
        limit, offset = limit or 20, offset or 0 # default
        return TaskModel.objects.all()[offset: offset + limit]

    @rpc(Integer, _returns=Task)
    def get_task(ctx, pk):
        try:
            return TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            raise ResourceNotFoundError("task")

    @rpc(Task, _returns=Task)
    def create_task(ctx, task):
        try:
            return TaskModel.objects.create(**task.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError("Task")

    @rpc(Task, _returns=Task)
    def update_task(ctx, task):
        return TaskModel.objects.filter(pk=task.pk).update(**task.as_dict())

app = Application(
    [
        TaskService,
    ],
    "project.app.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)
