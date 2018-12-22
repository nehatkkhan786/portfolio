from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	jobs = Job.objects.all()
	return render(request, 'jobs/home.html', {'jobs':jobs})
