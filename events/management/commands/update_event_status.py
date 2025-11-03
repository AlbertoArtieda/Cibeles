from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Event

class Command(BaseCommand):
    help = 'Desactiva eventos que ya han terminado'

    def handle(self, *args, **options):
        updated = Event.objects.filter(
            activo=True,
            fecha_fin__lt=timezone.now()
        ).update(activo=False)
        
        self.stdout.write(self.style.SUCCESS(f'Se desactivaron {updated} eventos'))