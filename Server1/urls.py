# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
]
