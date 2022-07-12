
from django.contrib import admin
from django.urls import path
from repairMyRoom import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('managment/', views.managment, name='managment'),

]
