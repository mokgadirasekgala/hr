from django.conf.urls import url

from leave import views

urlpatterns = [
    url(r'^trial$', views.trial, name='trial'),


]