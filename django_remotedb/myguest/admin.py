from django.contrib import admin

# Register your models here.
'''
MACui-MacBook-Pro:~ All$ cd /Users/All/Documents/work/workspace/pysou/django_remotedb
MACui-MacBook-Pro:django_remotedb All$ python manage.py makemigrations
MACui-MacBook-Pro:django_remotedb All$ python manage.py migrate
MACui-MacBook-Pro:django_remotedb All$ python manage.py createsuperuser
korea
test12345
'''
from myguest.models import Guest
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'regdate')
    
admin.site.register(Guest, GuestAdmin)