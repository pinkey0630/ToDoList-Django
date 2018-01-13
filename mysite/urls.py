from django.conf.urls import url
from django.contrib import admin
from todolist import views
#from views import todolist, complete, delete

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', views.todolist),
    url(r'^delete/(?P<pk>\d+)/', views.delete),
    url(r'^complete/(?P<pk>\d+)/', views.complete),
    
]
