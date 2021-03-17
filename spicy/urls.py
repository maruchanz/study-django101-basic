from django.urls import path
import spicy.views
from .views import DetailView
from .views import loginfunc, logout_view


app_name = 'spicy'

urlpatterns = [
    # path('', spicy.views.index, name='index'),
    path('', spicy.views.index, name='index'),
    path('kimetsu1/', spicy.views.kimetsu1, name='kimetsu1'),
    path('kimetsu2/', DetailView.as_view(), name='kimetsu2'),
    path('login/', loginfunc, name = 'login'),
    path('logout/', logout_view, name = 'logout')
    # path('login/', views.Login.as_view(), name = 'login'),
    # path('logout/', views.Logout.as_view(), name = 'logout'),
    # path('detail/', DetailView.as_view(), name ='detail')
]

