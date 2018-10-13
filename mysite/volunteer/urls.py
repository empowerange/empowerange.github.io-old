from django.conf.urls import url

from . import views

app_name = 'volunteer'

urlpatterns = [

     url(r'^', views.register, name='register'),
]
