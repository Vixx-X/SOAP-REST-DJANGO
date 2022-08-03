from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodoConfig(AppConfig):
    name = "project.apps.todo"
    label = "todo"
    verbose_name = _("todo")
