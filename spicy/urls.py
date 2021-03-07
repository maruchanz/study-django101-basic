from django.urls import path
from . import views

app_name = 'spicy'

urlpatterns = [
    path('', views.index, name='index'),
    path('kimetsu1/', views.kimetsu1, name='kimetsu1'),
    path('kimetsu2/', views.kimetsu2, name='kimetsu2'),
]
