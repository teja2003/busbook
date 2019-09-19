from django.shortcuts import render
from django.http import HttpResponse
from random import *
from .models import Register,Elite,Premium,Normal
from .forms import EliteForm,PremiumForm,NormalForm
# from django.contrib.auth.models import UserManager

# Create your views here.
def reg(request):
    if request.method=='POST':
        n=''
        for i in range(0,4):
            n=n+str(randint(0,9))
        Booking1_id=n
        
        #Customer_name=request.POST['b1']
        Username=request.POST['b2']
        Password=request.POST['b3']
        Membership_type=request.POST['b4']
       
        user=Register(Booking1_id=Booking1_id,Password=Password, Membership_type=Membership_type,Username=Username)
        user.save()
       
        return render(request, 'reg.html', {"msg":"GO TO THE LOGIN PAGE"})
    return render(request, 'reg.html')

def login(request):
    if request.method=='POST':
        Username=request.POST['b2']
        Password=request.POST['b3']
        try:
             dbuser=Register.objects.get(Username=Username, Password=Password)
             if dbuser:
                if dbuser.Membership_type=='Elite':
                     return render(request,'bus.html')

                elif dbuser.Membership_type=='Premium':
                     return render(request,'bus.html')

                elif dbuser.Membership_type=='Normal':
                     return render(request,'bus.html')

                else:
                    return render(request,'ticket.html')
             
        except Register.DoesNotExist:
            return render(request, 'login.html',{"msg":"UserName and Password Does Not Match"})
    return render(request, 'login.html')


def elite(request):
    form=EliteForm()
    if request.method=='POST':
        form=EliteForm(request.POST)
        if form.is_valid():
            n=''
            for i in range(0,6):
                n=n+str(randint(0,20))    
            Booking_id=n
            User=form.cleaned_data['User']
            Passenger_name=form.cleaned_data['Passenger_name']
            Bus_number=form.cleaned_data['Bus_number']
            Bus_type=form.cleaned_data['Bus_type']
            user=Elite(Booking_id=Booking_id, User=User,Bus_number=Bus_number,Bus_type=Bus_type)
            user.save()  
            return render(request,'ticket.html',{'form':form})
    return render(request, 'elite.html',{'form':form})

def premium(request):
    form=PremiumForm()
    if request.method=='POST':
        form=PremiumForm(request.POST)
        if form.is_valid():
            n=''
            for i in range(0,4):
                n=n+str(randint(0,9))    
            Booking_id=n
            User=form.cleaned_data['User']
            Passenger_name=form.cleaned_data['Passenger_name']
            Bus_number=form.cleaned_data['Bus_number']
            Bus_type=form.cleaned_data['Bus_type']
            user=Premium(Passenger_name=Passenger_name,Booking_id=Booking_id, User=User,Bus_number=Bus_number,Bus_type=Bus_type)
            user.save()
            return render(request, 'ticket.html',{'form':form})
    return render(request, 'premium.html',{'form':form})


def normal(request):
    form=NormalForm()
    if request.method=='POST':
        form=NormalForm(request.POST)
        if form.is_valid():
            n=''
            for i in range(0,4):
                n=n+str(randint(0,9))   
            Booking_id=n
            User=form.cleaned_data['User']
            Passenger_name=form.cleaned_data['Passenger_name']
            Bus_number=form.cleaned_data['Bus_number']
            Bus_type=form.cleaned_data['Bus_type']
            user=Normal(Booking_id=Booking_id, User=User,Bus_number=Bus_number,Bus_type=Bus_type)
            user.save()
            return render(request, 'ticket.html',{'form':form})
    return render(request, 'normal.html',{'form':form})

# def display(request):
#     query=request.GET['Q']:
#     object_list=elite.objects.filter(Q(id__icontains=query) | Q(Bus_number__icontains=query))
#     return render(request,'ticket.html', {'form':object_list, 'data':'elite'})