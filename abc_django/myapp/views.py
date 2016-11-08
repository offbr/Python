from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template.context import Context

# Create your views here.

def hello(request):
    name = "hello"
    msg ='world'
    ss ="<html><body>안녕%s,%s</body></html>"%(name,msg)
    return HttpResponse(ss)

def hello_template(request):
    name = '헬로'
    t = get_template('hello.html')
    hel = t.render(Context({'name':name}))
    return HttpResponse(hel)

def hello_template2(request):
    name = '월드'
    return render_to_response('hello.html',{'name':name})

def hello_image(request):
    return render_to_response('my.html')