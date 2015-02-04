from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from main_app import views


urlpatterns = patterns(
    '',
    url(r'^new/?$', views.landing, name='landing'),
)

