"""
URL configuration for Django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from firstApp.views import home, about
from secondApp.views import second_home, second_about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('second/', second_home, name='second_home'),
    path('second/about/', second_about, name='second_about')
]
