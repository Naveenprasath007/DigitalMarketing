"""template URL Configuration

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
from django.urls import path
from DigitalMarketing import views


urlpatterns = [
    path("admin/", admin.site.urls), 
    path("uploaderdashboard/<str:id>", views.uploaderdashboard),
    path("filterpage/<str:id>/<str:id1>", views.filterpage),
    path("createrupload/<str:id>", views.creater_upload),
    path("UserIndexpage", views.user_indexpage),
    path("approver/<str:id>", views.approver),
    path("approverview/<str:id>/<str:uid>", views.approver_view),
    path("status/<str:id>", views.status),
    path("statusview/<int:id>/<str:id1>", views.status_view),
    path("Download", views.download),
    path("Downloadvideo/<str:id>", views.download_video),
    path("DeleteVideo/<str:id>/<str:id1>", views.delete_video),
    path("uploadagain/<str:id>/<str:id1>", views.upload_again),   
]

