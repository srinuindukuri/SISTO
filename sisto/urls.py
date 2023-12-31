"""ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from clgweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('pylang/', views.pylang, name='pylang'),
    path('subscribe/', views.subscribe),
    path('pythonsoftware/', views.pythonsoftware, name='python software'),
    path('javasoftware/', views.javasoftware, name='java software'),
    path('csoftware/', views.csoftware, name='c software'),
    path('advancecsoftware/', views.advancecsoftware, name='advancec software'),
    path('pythonide/', views.pythonide, name='python ide'),




    path('login/', views.log_in, name='login'),
    path('logout/', views.logout, name='logout'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
