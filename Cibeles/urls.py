"""
URL configuration for Cibeles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from events.views import home_view, agenda_view, SalaView, ContactoView, evento_detalle

urlpatterns = [
    path('administracion2025/', admin.site.urls),
    path('', home_view, name='home'),
    path('agenda/', agenda_view, name='agenda'),
    path('sala/', SalaView.as_view(), name='sala'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('eventos/<slug:slug>/', evento_detalle, name='evento_detalle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files in development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()