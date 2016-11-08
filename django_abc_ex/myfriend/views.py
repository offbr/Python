from django.shortcuts import render, render_to_response
from myfriend.models import Friend

# Create your views here.
def main(request):
    return render_to_response('main.html')

def dbtest(request):
    return render_to_response('friendlist.html', {'friends':Friend.objects.all()})
