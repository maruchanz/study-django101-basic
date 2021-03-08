from django.urls import path
import spicy.views

app_name = 'spicy'

urlpatterns = [
    path('', spicy.views.index, name='index'),
    path('kimetsu1/', spicy.views.kimetsu1, name='kimetsu1'),
    path('kimetsu2/', spicy.views.kimetsu2, name='kimetsu2'),
    path('detail/', DetailView,as_view(), name ='detail'),
    # path('detail/<int:pk>/', DetailView.as_view(), name='detail'),

]
