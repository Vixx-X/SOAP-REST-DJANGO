""" Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

class RootView(TemplateView):
    template_name = "root.html"

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # todo REST
    path(
        "rest/",
        include(("project.apps.rest.urls", "project.apps.rest")),
    ),
    # todo SOAP
    path(
        "soap/",
        include(("project.apps.soap.urls", "project.apps.soap")),
    ),
    # root
    path(
        "",
        RootView.as_view(),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
