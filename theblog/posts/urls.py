from django.conf.urls import url

from .views import (
        posts_create,
        posts_delete,
        posts_detail,
        posts_list,
        posts_update,
)

urlpatterns = [
    url(r'^$', posts_list, name='list'),
    url(r'^create/$', posts_create, name='create'),
    url(r'^(?P<slug>[\w-]+)$', posts_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete, name="delete")
]
