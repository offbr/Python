'''
Created on 2016. 11. 4.

사용자 정의 url
'''
from django.conf.urls import url
from myapp import views
from django.shortcuts import render_to_response
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    #url(r'^$',views.hello, name='hello'),
    url(r'^aa',views.hello, name='hello'), #첫글자만 aa로 시작하면 됨.
    url(r'^bb',views.hello_template, name='hello_template'), #첫글자만 aa로 시작하면 됨.
    url(r'^cc',views.hello_template2, name='hello_template2'),
    url(r'^dd',views.hello_image),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
