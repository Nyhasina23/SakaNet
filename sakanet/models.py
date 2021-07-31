from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
    
class Utilisateur(models.Model):
    nom_user = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    nom = models.CharField(max_length=50,null=True)
    prenom = models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.nom+"  "+self.prenom


class Discussion(models.Model):
    nom_discussion = models.CharField(max_length=50 , null=True)
    liste_message= models.IntegerField(null=True)

    def __str__(self):
        return self.nom_discussion

class Message(models.Model):
    date_envoye = models.DateTimeField(auto_now_add=True)
    contenus = models.TextField(max_length=500)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)    
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.contenus


class Invitation(models.Model):
    liste_invitation = models.IntegerField(null=True)
    utilisateur = models.ForeignKey(Utilisateur , on_delete=models.CASCADE)

class Ami(models.Model):
     liste_amis = models.IntegerField(null=True)
     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
