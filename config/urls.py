"""config URL Configuration

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
from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('myadmin/', admin.site.urls),
    path('' , include('pages.urls')),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('accounts/' , include('pages.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', include('Adminpanel.urls')),  # مسیر اپ جدید

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

handler404 = 'pages.views.error_404_view'


