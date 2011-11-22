from horse.events.models import Event, School
from django.shortcuts import render_to_response

def homepage(request):
    events = Event.objects.order_by('-date')[:5]
    return render_to_response('homepage.html', {'events': events,})

def event_list(request):
    events = Event.objects.order_by('-date')
    return render_to_response('event.html', {'events': events,})

def detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render_to_response('detail.html', {'event':event})
