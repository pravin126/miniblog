"""
URL configuration for miniblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("dashbord/", views.dashbord, name='dashbord'),
    path("signup/", views.user_signup, name='signup'),
    path("user_login/", views.user_login, name='user_login'),
    path("user_logout/", views.user_logout, name='user_logout'),
    path("addpost/", views.addpost, name='addpost'),
    path("updatepost/<int:id>/", views.updatepost, name='updatepost'),
    path("deletepost/<int:id>/", views.deletepost, name='deletepost'),
]
