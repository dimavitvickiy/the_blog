from django.conf.urls import url

from .views import (
        comment_thread,
        comment_delete,
        comment_edit
)

urlpatterns = [
    url(r'^(?P<id>\d+)$', comment_thread, name='thread'),
    url(r'^(?P<id>\d+)/edit/$', comment_edit, name="edit"),
    url(r'^(?P<id>\d+)/delete/$', comment_delete, name="delete")
]