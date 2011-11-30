from horse.schools.models import Season, School
from django.shortcuts import render_to_response

def school_list(request):
    schools = School.objects.order_by('school')
    return render_to_response('school/school.html', {'schools': schools,})

def detail(request, school_id):
    school = School.objects.get(id=school_id)
    return render_to_response('school/detail.html', {'school': school})

