
from typing import Union
from django import forms
from django.forms import widgets 
from django.core import validators


class Student(forms.Form):
   firstname=forms.CharField()
   lastname=forms.CharField()
   fullname=forms.CharField()
   EmailID=forms.EmailField()
   Mobileno=forms.IntegerField()
   CreatePassword=forms.CharField(widget=forms.PasswordInput)
   ConfirmPassword=forms.CharField(widget=forms.PasswordInput)
   def clean(self):
     entire_data=super().clean() 
     P=entire_data['CreatePassword']
     RP=entire_data['ConfirmPassword']
     if(P!=RP):
        raise forms.ValidationError("Mismatch in password")
     m=entire_data['Mobileno'] 
     p1=str(m)
     if(len(p1)>10):
         raise forms.ValidationError("mobile no should be exact 10 Digit")  

class studentlogin(forms.Form):
   username=forms.CharField()
   password=forms.CharField(widget=forms.PasswordInput)
   def clean_FieldName(self):
      username=self.cleaned_data['username']
      fullname=self.cleaned_data['fullname']
      if(username!=fullname):
         raise forms.ValidationError("username should be equal to fullname")



 
          

   