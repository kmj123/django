from django.shortcuts import render
from event.models import Event

def event(request):
    qs = Event.objects.all()
    context = {'event':qs}
    return render(request,'event/list.html',context)
