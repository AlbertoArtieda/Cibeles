from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Event

def home_view(request):
    # Filtrar los próximos 8 eventos activos
    eventos = Event.objects.filter(activo=True).order_by('fecha_inicio')[:8]
    
    return render(request, 'home.html', {'eventos': eventos})

def agenda_view(request):    
    # Iniciar con todos los eventos activos
    eventos = Event.objects.filter(activo=True).order_by('fecha_inicio')
        
    return render(request, 'agenda.html', {'eventos': eventos})

def evento_detalle(request, slug):
    evento = get_object_or_404(Event, slug=slug)
    return render(request, 'evento.html', {'evento': evento})

class SalaView(TemplateView):
    template_name = 'sala.html'

class ContactoView(TemplateView):
    template_name = 'contacto.html'
