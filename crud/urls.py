"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from crud.views import call_home
from main.views import add_detail,retrive,delete,update,saved_successfully,deleted_successfully
urlpatterns = [
    path('secure/', admin.site.urls),
    path('', call_home),
    path('create', add_detail),
    path('retrive', retrive),
    path('delete', delete),
    path('update', update),
    path('saved', saved_successfully),
    path('deleted', deleted_successfully),
]
