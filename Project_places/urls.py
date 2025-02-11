"""Project_places URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from places.views import home_view, create_view, edit_view, delete_view, list_read_view, read_view, list_edit_view, list_delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create', create_view),
   # path('edit', edit_view),
    path('edit/<int:my_id>/', edit_view),
    path('delete/<int:my_id>/', delete_view),
    path('read/<int:my_id>/', read_view),
    path('list_read', list_read_view),
    path('list_edit', list_edit_view),
    path('list_delete', list_delete_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
