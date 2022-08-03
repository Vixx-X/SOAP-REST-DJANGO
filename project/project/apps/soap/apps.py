from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SoapConfig(AppConfig):
    name = "project.apps.soap"
    label = "soap"
    verbose_name = _("soap")
