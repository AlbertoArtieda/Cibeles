
# Cibeles - Gestión de Eventos

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

Sistema para la gestión de eventos, venta de entradas y visualización de la agenda de actividades para la sala Cibeles. Desarrollado con Django 5.2.4.

## 🚀 Características

- Gestión completa de eventos con fechas, precios y descripciones
- Sistema de precios anticipados y en taquilla
- Galería de imágenes para cada evento
- Integración con redes sociales (Instagram, YouTube)
- Panel de administración personalizado
- Diseño responsive para móviles y escritorio
- Sistema de categorización de eventos

## 🛠️ Requisitos

- Python 3.8+
- Django 5.2.4
- Pillow (para el manejo de imágenes)
- Virtualenv (recomendado)

## 🚀 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/AlbertoArtieda/Cibeles.git
   cd Cibeles
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuración**
   - Copiar `.env.example` a `.env`
   - Configurar las variables de entorno necesarias

5. **Migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

7. **Iniciar servidor**
   ```bash
   python manage.py runserver
   ```

## 🏗️ Estructura del Proyecto

```
Cibeles/
├── Cibeles/               # Configuración del proyecto
├── events/                # Aplicación principal de eventos
├── static/                # Archivos estáticos (CSS, JS, imágenes)
│   ├── css/              
│   ├── img/              
│   └── video/            
├── templates/             # Plantillas HTML
├── media/                 # Archivos subidos por usuarios
└── manage.py             
```

## 🌐 Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

```
DEBUG=True
SECRET_KEY=tu_clave_secreta_aqui
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Contribución

Las contribuciones son bienvenidas. Por favor, lee nuestras pautas de contribución antes de enviar un pull request.

## 📧 Contacto

Para más información, contacta con a.artiedalopez@gmail.com.
