from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Schedule

def schedule_view(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedule/schedule_list.html', {'schedules': schedules})
