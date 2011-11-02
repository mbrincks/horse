from horseproject.eventsapp.models import Event, School
from django.shortcuts import render_to_response

def homepage(request):
    event_list = Event.objects.order_by('date')
    return render_to_response('homepage.html', {'events': events,})
