from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.apples, name="apples"),
    url(r'^(?P<apple_id>[0-9]+)/$', views.detail, name='detail'),
]