# from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from tests.views import index

urlpatterns = [url(r"^index/", index)]
