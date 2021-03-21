from django.urls import path
from . import views

urlpatterns = [
    path('', views.zakaz_list, name='zakaz_list'),
    path('<int:pk>/', views.zakaz_detail, name='zakaz_detail'),
    path('new/', views.zakaz_new, name='zakaz_new'),
    path('<int:pk>/edit/', views.zakaz_edit, name='zakaz_edit'),
    path('detal/', views.detal_list, name='detal_list'),
    path('detal/<int:pk>/', views.detal_detail, name='detal_detail'),
    path('detal/new/', views.detal_new, name='detal_new'),
    path('detal/<int:pk>/edit/', views.detal_edit, name='detal_edit'),
]

