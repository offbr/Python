'''
Created on 2016. 11. 7.
'''
from django.conf.urls import url
from gtapp import views

urlpatterns = [
    url(r'^insert/$', views.InsertFunc, name='InsertFunc')    
]