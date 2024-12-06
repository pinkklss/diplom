"""
URL configuration for diplom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from users.views import register_user, register_superuser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register_user'),
    path('superuser_register/', superuser_register, name='superuser_register'),
    path('create-order/', views.create_order, name='create_order'),
    path('product-list/', views.create_product, name='product_list'),

]
