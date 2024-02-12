"""
URL configuration for contactbook project.

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
from django.urls import path
from contact_add.views import *

urlpatterns = [
    path('', home),
    path('register', register),
    path('view_user/', view_user),
    path('deshbord/', deshbord),
    path('logout/', logout),
    # path('contact_add',contact_add),
    path('contact_add/', add_cant),
    path('delete-data/<int:del_id>', delete_data),
    path('edit-data/<int:edit_id>', edit_data),
    path('edit-pro/<int:edit_pro>', edit_pro),
    path('admin/', admin.site.urls),
]
