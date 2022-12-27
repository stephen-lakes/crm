"""teal_crm URL Configuration

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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from core.views import index, about
from userprofile.views import signup

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('about/', about, name='about'),
    path('sign-up/', signup, name='signup'),
    path('log-in/', LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
