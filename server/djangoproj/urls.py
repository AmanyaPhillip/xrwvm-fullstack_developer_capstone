"""
URL configuration for djangoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include # E231: missing whitespace after ',' ; E501: Line too long.
from django.conf import settings # Add these for static files in development
from django.conf.urls.static import static # Add these for static files in development

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('djangoapp/', include('djangoapp.urls')), # E231: missing whitespace after ',' ; E501: Line too long.
    path('', include('djangoapp.urls')), # This makes your 'index' route accessible at the root
=======
    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('login/', TemplateView.as_view(template_name="index.html")),
    path('register/', TemplateView.as_view(template_name="index.html")),
>>>>>>> parent of 749909e (Module 4)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
