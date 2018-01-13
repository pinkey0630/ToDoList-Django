from django.conf.urls import url
from django.contrib import admin
from views import todolist, complete, delete

urlpatterns = [
    #url(r'^$', views.index, name = 'index'),
    url(r'^admin/', admin.site.urls),
    url(r'^$', todolist),
    url(r'^complete/(?P<pk>\d+)/', complete),
    url(r'^delete/(?P<pk>\d+)/', delete),

]
