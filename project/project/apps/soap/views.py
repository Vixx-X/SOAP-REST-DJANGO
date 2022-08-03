from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from spyne.error import ResourceNotFoundError, ResourceAlreadyExistsError
from spyne.model.primitive import Integer
from spyne.service import Service
from spyne.protocol.soap import Soap11
from spyne.application import Application
from spyne.decorator import rpc
from spyne.util.django import DjangoService

from project.apps.todo.models import Task as TaskModel

from .serializers import Task


class TaskService(Service):
    @rpc(Integer, _returns=Task)
    def get_task(ctx, pk):
        try:
            return TaskModel.objects.get(pk=pk)
        except TaskModel.DoesNotExist:
            raise ResourceNotFoundError("Task")

    @rpc(Task, _returns=Task)
    def create_task(ctx, task):
        try:
            return TaskModel.objects.create(**task.as_dict())
        except IntegrityError:
            raise ResourceAlreadyExistsError("Task")


class ExceptionHandlingService(DjangoService):
    """
    Service for testing exception handling
    """

    @rpc(_returns=Task)
    def raise_does_not_exist(ctx):
        return TaskModel.objects.get(pk=-1)

    @rpc(_returns=Task)
    def raise_validation_error(ctx):
        raise ValidationError(None, "Invalid.")


app = Application(
    [
        TaskService,
        ExceptionHandlingService,
    ],
    "project.app.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)
