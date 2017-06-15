from django.conf.urls import url
from django.contrib.auth import views as auth_views

from leave import views

urlpatterns = [
    url(r'^trial$', views.trial, name='trial'),
    url(r'^$', views.index, name='index'),
    url(r'^login/$',auth_views.login, {'template_name': 'leave/login.html'},name='login'),
    url(r'^leave$', views.log_leave, name='logleave'),


]