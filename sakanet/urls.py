from django.urls import path
from . import  views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('index', views.index, name="index"),
    path('logout', views.user_logout, name="user_logout"),
    path('login', views.user_login, name="user_login"),
    path('register', views.register, name="register"),
    path('detail/<message_id>', views.detail, name="detail"),
    path('message', views.message, name="message"),
    path('publication', views.publication, name="publication"),
    path('discussion/<id>', views.discussion, name="discussion"),
    path('', views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
