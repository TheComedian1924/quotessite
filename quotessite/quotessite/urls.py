"""
URL configuration for quotessite project.

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
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addquote/', views.addquote, name = 'addquote'),
    path('top/', views.showtop, name = 'top'),
    path('like/<int:quote_id>', views.like, name = 'like'),
    path('dislike/<int:quote_id>', views.dislike, name = 'dislike'),
    path('', views.index, name = 'home')
]
