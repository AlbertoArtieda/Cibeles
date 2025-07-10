from django.shortcuts import render
from .models import Event
from django.utils import timezone
from datetime import timedelta

def home_view(request):
    return render(request, 'home.html')

def agenda_view(request):    
    eventos = Event.objects.all().order_by('fecha_inicio')
    return render(request, 'agenda.html', {'eventos': eventos})