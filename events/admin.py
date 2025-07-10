from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import Event

class EventoActivoFilter(SimpleListFilter):
    title = _('Estado')
    parameter_name = 'estado'

    def lookups(self, request, model_admin):
        return (
            ('activo', _('Activo')),
            ('inactivo', _('Inactivo')),
            ('futuro', _('Futuro')),
            ('pasado', _('Pasado')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'activo':
            return queryset.filter(activo=True)
        if self.value() == 'inactivo':
            return queryset.filter(activo=False)
        if self.value() == 'futuro':
            return queryset.filter(fecha_inicio__gt=timezone.now())
        if self.value() == 'pasado':
            return queryset.filter(fecha_fin__lt=timezone.now())

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'categoria', 'sala', 'fecha_inicio', 'fecha_fin', 'activo', 'creado_por', 'actualizado_por'
    )
    list_filter = (
        'categoria', 
        'sala', 
        'activo',
        EventoActivoFilter,
        'creado_en',
        'actualizado_en'
    )
    search_fields = (
        'nombre', 
        'descripcion', 
        'ubicacion', 
        'instagram', 
        'youtube'
    )
    date_hierarchy = 'fecha_inicio'
    ordering = ('-fecha_inicio',)
    readonly_fields = ('creado_en', 'actualizado_en', 'creado_por', 'actualizado_por')
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'slug', 'descripcion', 'categoria', 'sala', 'activo')
        }),
        ('Fechas y Horarios', {
            'fields': ('fecha_inicio', 'fecha_fin')
        }),
        ('Ubicación y Precios', {
            'fields': ('ubicacion', 'precio_anticipado', 'precio_taquilla')
        }),
        ('Medios', {
            'fields': ('imagen', 'video', 'instagram', 'youtube')
        }),
        ('Enlaces', {
            'fields': ('link_entradas',)
        }),
        ('Auditoría', {
            'fields': ('creado_por', 'creado_en', 'actualizado_por', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(creado_por=request.user)
        return qs

    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.has_perm('events.add_event')

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj.creado_por == request.user

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return True
        return request.user.is_superuser or obj.creado_por == request.user

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creado_por = request.user
        obj.actualizado_por = request.user
        super().save_model(request, obj, form, change)
