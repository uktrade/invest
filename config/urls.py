from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
]
