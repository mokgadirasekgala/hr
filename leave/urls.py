from django.conf.urls import url
from django.contrib.auth import views as auth_views

from leave import views

urlpatterns = [
    url(r'^newemployee$', views.create_employee, name='createemployee'),
    url(r'^$', views.index, name='index'),
    url(r'^leave$', views.log_leave, name='logleave'),


]