from spyne.server.django import DjangoView
from django.urls.conf import path

from . import views

urlpatterns = [
    path("", DjangoView.as_view(application=views.app)),
]
