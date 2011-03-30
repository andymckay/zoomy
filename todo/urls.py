from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^add$', 'todo.views.add', name='todo.add'),
    url(r'^edit/(?P<pk>\d+)$', 'todo.views.edit', name='todo.edit'),
    url(r'^$', 'todo.views.list', name='todo.list'),
)
