from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app.forms import *
from app.models import *
from app.serializers import *
from rest_framework import viewsets
from app.serializers import *
from rest_framework.response import Response

# Create your views here.



def home(request):
    if request.session.get('username'):
        username = request.session.get('username')
        d={'username' : username}
        return render(request,'home.html',d)
    return render(request,'home.html')




def Register(request):
    UO =UserForm()
    d ={'UO' : UO}
    if request.method == 'POST':
        UFO = UserForm(request.POST)
        if UFO.is_valid():
            NUFO=UFO.save(commit=False)
            password=UFO.cleaned_data['password']
            NUFO.set_password(password)
            NUFO.save()
            return HttpResponse("Registeration done successfully")
    return render(request,'register.html',d)



def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('invalid username or password')
    

    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def insert_data(request):
    d = {'FO' : FreedomFightersForm()}
    if request.method == 'POST' and request.FILES:
        
        FOD = FreedomFightersForm(request.POST,request.FILES)
        if FOD.is_valid():
            FOD.save()
            return HttpResponse("The data is inseted succfuly")
        else:
            return HttpResponse("The data is invalid")
    return render(request,'insert_data.html',d)


class FreedomFightersData(viewsets.ViewSet):
    def list(self,request):
        ADO=FreedomFighters.objects.all()
        SJD=FreedomFightersMS(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)

    def retrieve(self,request,pk):
        TO=FreedomFighters.objects.get(pk=pk)
        SDO=FreedomFightersMS(TO)
        return Response(SDO.data)

    def update(self,request,pk):
        SPO=FreedomFighters.objects.get(pk=pk)
        SPD=FreedomFightersMS(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Fredom fighters is updated'})
        else:
            return Response({'Failed':'Fredom fighters is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=FreedomFighters.objects.get(pk=pk)
        SPD=FreedomFightersMS(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Fredom fighters is updated'})
        else:
            return Response({'Failed':'Fredom fighters is Not Updated'})
    def destroy(self,request,pk):
        FreedomFighters.objects.get(pk=pk).delete()
        return Response({'Deleted':'Fredom fighters data is deleted'})
