from django.shortcuts import render,redirect,get_object_or_404
from sakanet.models import *
from sakanet.forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import json
from django.http.response import JsonResponse
from django.template import loader
def index(request):
    message = None
    form = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = MessagesForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False) # Return an object without saving to the DB
                obj.utilisateur = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
                obj.save() # Save the final "real form" to the DB
            else:
                print("ERROR : Form is invalid")
                print(form.errors)
    form = MessagesForm()
            #     print("ERROR")
    
    message = Message.objects.order_by('-date_envoye')[:3]
    return render(request,'index.html',{'messages':message,'form':form})

def profil(request,id):
    user_profile = None
    form = None
    message = None
    user_profile = get_object_or_404(User, id=id)
    form = MessagesForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False) # Return an object without saving to the DB
            obj.utilisateur = User.objects.get(pk=request.user.id) # Add an author field which will contain current user's id
            obj.save() # Save the final "real form" to the DB
        else:
            print("ERROR : Form is invalid")
            print(form.errors)
    message = Message.objects.order_by('-date_envoye')[:3]
    return render(request, 'profil.html', {'user_profile':user_profile,'form':form,'message':message})

@login_required
def discussion(request,pk):
    other_user = get_object_or_404(User,pk=pk)
    messages = Message.objects.filter(
        Q(receiver=request.user,sender=other_user)
    )
    messages.update(seen=True)
    messages = messages | Message.objects.filter(Q(receiver=other_user,sender=request.user))
    return render(request, 'discussion.html',{"other_user":other_user, "messages":messages})

@login_required
def ajax_load_messages(request,id):
    other_user = get_object_or_404(User,id=id)
    messages = Message.objects.filter(seen=False).filter(
        Q(receiver=request.user,sender=other_user)
    )   
    message_list = [{
        "sender": message.sender.username,
        "message": message.message,
        "sent" : message.sender == request.user
    } for message in messages]
    messages.update(seen=True)

    if request.method == 'POST':
        message = json.loads(request.body)
        m = Message.objects.create(receiver=other_user, sender=request.user,message=message)
        message_list.append({
            "sender": request.user.username,
            "message":m.message,
            "sent":True,
        })
    return JsonResponse(message_list, safe=False)



def publication(request):
    contenus_pub = None
    forms = None
    users = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            forms = PubForm(request.POST)
            if forms.is_valid():
                obj = forms.save(commit=False) # Return an object without saving to the DB
                obj.utilisateur = User.objects.get(pk=request.user.id) # Add an user field which will contain current user's id
                obj.save() # Save the final "real form" to the DB
            else:
                print("ERROR : Form is invalid")
                print(forms.errors)
            #     print("ERROR")
    
    forms = PubForm()
    pub = Publication.objects.order_by('-date_envoye')[:3]
    users = User.objects.filter()
    return render(request,'publication.html',{'publication':pub,'form_field':forms,'users':users})

# def listMessage(request):
    # message = Message.objects.filter()
    # formated_message =  ["<h1>Nom du profil : {} </h1> <br><br><li> Nom = {} <br> Message = {} </li>".format(mes.profil 
    # ,mes.utilisateur ,mes.contenus ) for mes in message  ] 
    # messages = ["<ul>{}</ul>".format("\n".join(formated_message))  ]
    # return HttpResponse(messages)
    # # disc = profil.objects.all()
    # disValue =[ " contenus = {} ".format( discs.nom_profil for discs in disc   )]
    # return HttpResponse(disc)


def detail(request, message_id):
    message = Message.objects.get(pk=message_id)
    users =  " ".join([ user.nom  for user in  message.objects.all() ])
    result = "Le nom = {} , son message est = {} ".format(users , message.contenus )
    return HttpResponse(result)

def message(request,id):

    user_profile = get_object_or_404(User, id=id)
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
            return redirect('publication')
        messages.error(request, "Registration failed")
        return redirect('register')    
    else:
        user_register = UserRegister()
    return render(request,'sakanet/register.html',{'user_register':user_register})

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
                return redirect('publication')
            else:
                messages.error(request, 'Invalid login')
        else:
               messages.error(request, 'Invalid login')
    form = AuthenticationForm()
    # template = loader.get_template('sakanet/sakanet_login.html')
    # return HttpResponse(template.render({'login_form':form},request=request))
    return render(request, 'sakanet/login.html',{'login_form':form})

def user_logout(request):
    logout(request)
    messages.info(request,"You have successfully logged out.")
    return redirect('user_login')