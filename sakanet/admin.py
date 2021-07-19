from django.contrib import admin

# Register your models here.
from .models import Utilisateur,Message,Discussion,Invitation,Ami

admin.site.register(Utilisateur)
admin.site.register(Discussion)
admin.site.register(Message)
admin.site.register(Invitation)
admin.site.register(Ami)