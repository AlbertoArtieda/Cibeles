from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    CATEGORIES = [
        ('concierto', 'Concierto'),
        ('clubbing', 'Clubbing'),
        ('cancelado', 'Cancelado')
    ]
    
    SALAS = [
        ('Sala 1', 'Sala 1'),
        ('Sala 2', 'Sala 2')
    ]

    nombre = models.CharField(
        max_length=255,
        help_text='Nombre del evento'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        help_text='URL amigable para el evento'
    )
    descripcion = models.TextField(
        help_text='Descripción detallada del evento'
    )
    fecha_inicio = models.DateTimeField(
        help_text='Fecha y hora de inicio del evento'
    )
    fecha_fin = models.DateTimeField(
        help_text='Fecha y hora de fin del evento'
    )
    imagen = models.ImageField(
        upload_to='eventos/imagenes/',
        blank=True,
        null=True,
        help_text='Imagen principal del evento'
    )
    video = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text='URL del video promocional'
    )
    link_entradas = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text='Enlace para comprar entradas'
    )
    precio_anticipado = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text='Precio de la entrada con anticipación'
    )
    precio_taquilla = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text='Precio de la entrada en taquilla'
    )
    ubicacion = models.CharField(
        max_length=255,
        help_text='Ubicación del evento'
    )
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIES,
        help_text='Categoría del evento'
    )
    sala = models.CharField(
        max_length=10,
        choices=SALAS,
        help_text='Sala donde se realiza el evento'
    )
    instagram = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        help_text='URL del perfil de Instagram'
    )
    youtube = models.URLField(
        max_length=255,
        blank=True,
        null=True,
        help_text='URL del canal de YouTube'
    )
    activo = models.BooleanField(
        default=True,
        help_text='Indica si el evento está activo'
    )
    creado_en = models.DateTimeField(
        auto_now_add=True,
        help_text='Fecha de creación del evento'
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        help_text='Fecha de última actualización'
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='eventos_creados',
        help_text='Usuario que creó el evento'
    )
    actualizado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='eventos_actualizados',
        help_text='Usuario que actualizó el evento'
    )

    def clean(self):
        # Validación de fechas
        if self.fecha_fin <= self.fecha_inicio:
            raise ValidationError('La fecha de fin debe ser posterior a la fecha de inicio')
        
        # Validación de precios
        if self.precio_anticipado is not None and self.precio_taquilla is not None:
            if self.precio_anticipado < 0 or self.precio_taquilla < 0:
                raise ValidationError('Los precios no pueden ser negativos')
        
        # Validación de URLs
        if self.video and not self.video.startswith(('http://', 'https://')):
            raise ValidationError('La URL del video debe ser una URL válida')
        
        if self.link_entradas and not self.link_entradas.startswith(('http://', 'https://')):
            raise ValidationError('El enlace de entradas debe ser una URL válida')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-fecha_inicio']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
    instagram = models.CharField(max_length=255, blank=True, null=True)
    youtube = models.CharField(max_length=255, blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
