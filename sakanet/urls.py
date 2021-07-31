from django.urls import path
from . import  views

urlpatterns = [
    path('register', views.register, name="register"),
    path('detail/<message_id>', views.detail, name="detail"),
    path('message', views.listMessage, name="listMessage"),
    path('', views.index, name="index"),
]
