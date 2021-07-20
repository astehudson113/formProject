
from django.shortcuts import render
from myApp.forms import Student
from myApp.forms import studentlogin
# Create your views here.

def view1(request):
    f=Student()
    if request.method=="POST":
      f=Student(request.POST)
      if f.is_valid():
       firstname=f.cleaned_data['firstname']  
       lastname=f.cleaned_data['lastname']
       fullname=f.cleaned_data['fullname']
       EmailID=f.cleaned_data['EmailID']
       Mobileno=f.cleaned_data['Mobileno']
       CreatePassword=f.cleaned_data['CreatePassword']
       ConfirmPassword=f.cleaned_data['ConfirmPassword']
       d={'firstname1':firstname,'lastname1':lastname,'fullname1':fullname,'EmailID1':EmailID,'Mobileno1':Mobileno,'CreatePassword1':CreatePassword,'ConfirmPassword1':ConfirmPassword}
       return render(request,'myApp/Output.html',d)
    d={'form':f}  
    return render(request,'myApp/input.html',d)

def view2(request):
    f=studentlogin()
    if request.method=="POST":
       f=studentlogin(request.POST)
       if f.is_valid():
        username=f.cleaned_data['username']
        password=f.cleaned_data['password']
        d={'username1':username,'password1':password}
        return render(request,'myApp/logout.html',d)
   
    d={'form':f}
    return render(request,'myApp/login.html',d)
