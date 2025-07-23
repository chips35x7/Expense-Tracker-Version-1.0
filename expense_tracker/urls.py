"""
URL configuration for expense_tracker project.

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
from django.urls import path, include
from django.conf import settings

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
    )

from accounts.views import CustomEmailConfirmView

API_VERSION = 'api/v1'

urlpatterns = [
    # Admin url path
    path('admin/', admin.site.urls),

    # Authentication Endpoints
    path(f'{API_VERSION}/auth/', include('dj_rest_auth.urls')),
    path(f'{API_VERSION}/auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # Overiding the confirm email view that ships with allauth by default
    path(f'{API_VERSION}/auth/registration/account-confirm-email/<key>', CustomEmailConfirmView.as_view(), name='account_confirm_email'),

    # Other Endpoints
    path(f'{API_VERSION}/', include('expenses.urls')),

    # Schema and documentation endpoints
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/redoc', SpectacularRedocView.as_view(url_name="schema"), name='redoc'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name="schema"), name='swagger-ui'),
]

# Using browser based session authentication in development 
if settings.DEBUG:
    urlpatterns.append(path('api/auth/', include('rest_framework.urls')),)