"""vitalityone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Admin page honeypot
    # path('admin/', include('admin_honeypot.urls')),

    # Our actual admin page
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('termsCondition/', views.termsCondition, name='termsCondition'),
    path('policy/', views.policy, name='Policy'),
    path('about/', include('about.urls')),
    path('fitness/', include('fitness.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('health/', include('health.urls')),
    path('tools/', include('tools.urls')),
    path('register/', include('loginsystem.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
