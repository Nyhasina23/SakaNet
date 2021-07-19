from django.shortcuts import render
from sakanet.models import *

from django.http import HttpResponse
# Create your views here.
        
def index(request):
    message = " Hello wolrd "
    return HttpResponse(message)

def listMessage(request):
    message = Message.objects.filter()
    formated_message =  ["<h1>Nom du discussion : {} </h1> <br><br><li> Nom = {} <br> Message = {} </li>".format(mes.discussion 
    ,mes.utilisateur ,mes.contenus ) for mes in message  ] 
    messages = ["<ul>{}</ul>".format("\n".join(formated_message))  ]
    return HttpResponse(messages)
    # disc = Discussion.objects.all()
    # disValue =[ " contenus = {} ".format( discs.nom_discussion for discs in disc   )]
    # return HttpResponse(disc)


def detail(request, message_id):
    message = Message.objects.get(pk=message_id)
    users =  " ".join([ user.nom  for user in  message.objects.all() ])
    result = "Le nom = {} , son message est = {} ".format(users , message.contenus )
    return HttpResponse(result)