from horse.riders.models import Rider, Season
from django.shortcuts import render_to_response

def rider_list(request):
    rider = Rider.objects.order_by('name')
    return render_to_response('riders/riders.html', {'rider':rider})

def detail(request, rider_id):
    rider = Rider.objects.get(id=rider_id)
    return render_to_response('riders/detail.html', {'rider':rider})
