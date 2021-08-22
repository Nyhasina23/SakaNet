from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Utilisateur,Publication,Message,Discussion,Invitation,Ami

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username','email','first_name','last_name','is_staff',
        'photo','isOnline'
    )

    fieldsets = (
        (None,{
            'fields': ('username','password')
        }),
        ('Personal info',{
            'fields':('first_name','last_name','email')
        }),
        ('Perimssions',{
            'fields':(
                'is_active','is_staff','is_superuser',
                'groups','user_permissions'
            )
        }),
        ('Important dates',{
            'fields':('last_login','date_joined')
        }),
        ('Additional info',{
            'fields':('photo','isOnline')
        })
    )
    add_fieldsets = (
        (None,{
            'fields': ('username','password1','password2')
        }),
        ('Personal info',{
            'fields':('first_name','last_name','email')
        }),
        ('Perimssions',{
            'fields':(
                'is_active','is_staff','is_superuser',
                'groups','user_permissions'
            )
        }),
        ('Important dates',{
            'fields':('last_login','date_joined')
        }),
        ('Additional info',{
            'fields':('photo','isOnline')
        })
    )

admin.site.register(Utilisateur)
# admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Publication)
admin.site.register(Discussion)
admin.site.register(Message)
admin.site.register(Invitation)
admin.site.register(Ami)
