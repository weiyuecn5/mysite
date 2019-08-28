"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from pad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('wy/', views.wy, name='wy'),
    path('addshuju/', views.addshuju, name='addshuju'),
    path('add/<wyid>/<zhid>/<st>/<dj>/<cw>/',views.add,name='add'),#/账号编号/石头数量/等级/宠物编号/
    path('delshuju/<zhid>/', views.delshuju, name='delshuju'),
    path('upshuju/', views.upshuju,name='upshuju'),
    path('qd/', views.qd,name='qd'),
]
