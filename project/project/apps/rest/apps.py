from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RestConfig(AppConfig):
    name = "project.apps.rest"
    label = "rest"
    verbose_name = _("rest")
