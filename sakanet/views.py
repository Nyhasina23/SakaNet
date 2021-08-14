from django.shortcuts import render,redirect
from sakanet.models import *
from sakanet.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
        
def index(request):
    if request.method == 'POST':
        message = None
        form = None
        form = MessagesForm(request.POST or None)
        if form.is_valid() :
            form.save()
            return redirect('index')
    else:
        form = MessagesForm()
    
    message = Message.objects.order_by('-date_envoye')[:3]
    return render(request,'index.html',{'messages':message,'form':form})

# def listMessage(request):
    # message = Message.objects.filter()
    # formated_message =  ["<h1>Nom du discussion : {} </h1> <br><br><li> Nom = {} <br> Message = {} </li>".format(mes.discussion 
    # ,mes.utilisateur ,mes.contenus ) for mes in message  ] 
    # messages = ["<ul>{}</ul>".format("\n".join(formated_message))  ]
    # return HttpResponse(messages)
    # # disc = Discussion.objects.all()
    # disValue =[ " contenus = {} ".format( discs.nom_discussion for discs in disc   )]
    # return HttpResponse(disc)


def detail(request, message_id):
    message = Message.objects.get(pk=message_id)
    users =  " ".join([ user.nom  for user in  message.objects.all() ])
    result = "Le nom = {} , son message est = {} ".format(users , message.contenus )
    return HttpResponse(result)

def message(request):
    if request.method == 'POST':
        form = MessagesForm(request.POST or None)
        # userlogForm = MessagesForm(request.POST , instance=request.user)
        if form.is_valid() :
            form.save()
            # userlogForm = Message.objects.get(user=request.user)
            # userlogForm = request.user.userlogForm
            # userlogForm.utilisateur = "None"
            # userlogForm.save()
            
            return redirect('index')
    else:
        form = MessagesForm()
    return render(request , 'index.html',{'form' : form}) 

def register(request):
    if request.method == 'POST':
        user_register = UserRegister(request.POST)
        if  user_register.is_valid():
            user = user_register.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect('index')
        messages.error(request, "Registration failed")
        return redirect('register')    
    else:
        user_register = UserRegister()
    return render(request,'register.html',{'user_register':user_register})

def user_login(request):
    if request.method == 'POST':
        form  = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are logged in {username}")
                return redirect('index')
            else:
                messages.error(request, 'Invalid login')
        else:
               messages.error(request, 'Invalid login')
    form = AuthenticationForm()
    return render(request, 'login.html',{'login_form':form})

def user_logout(request):
    logout(request)
    messages.info(request,"You have successfully logged out.")
    return redirect('index')