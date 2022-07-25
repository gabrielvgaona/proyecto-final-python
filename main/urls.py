from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]

urlpatterns += staticfiles_urlpatterns()