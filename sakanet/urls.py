from django.urls import path
from . import  views

urlpatterns = [
    path('index', views.index, name="index"),
    path('logout', views.user_logout, name="user_logout"),
    path('login', views.user_login, name="user_login"),
    path('register', views.register, name="register"),
    path('detail/<message_id>', views.detail, name="detail"),
    path('message', views.listMessage, name="listMessage"),
    path('', views.index, name="index"),
]
