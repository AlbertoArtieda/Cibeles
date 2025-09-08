from django.shortcuts import render
from .models import Event
from django.utils import timezone
from datetime import timedelta

def home_view(request):
    # Filtrar los próximos 8 eventos activos
    eventos = Event.objects.filter(activo=True).order_by('fecha_inicio')[:8]
    
    return render(request, 'home.html', {'eventos': eventos})

def agenda_view(request):    
    # Iniciar con todos los eventos activos
    eventos = Event.objects.filter(activo=True).order_by('fecha_inicio')
        
    return render(request, 'agenda.html', {'eventos': eventos})