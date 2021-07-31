from django.shortcuts import render,redirect
from sakanet.models import *
from sakanet.forms import *

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

def register(request):
    if request.method == 'POST':
        user_register = UserRegister(request.POST)
        if  user_register.is_valid():
            user_register.save()
            return redirect('register')
            
    else:
        user_register = UserRegister()
    return render(request,'loginForm.html',{'user_register':user_register})