
from django import forms 
from django.core import validators
def validation_for_a(data):
    if data.lower().startswith('a') :
        raise forms.ValidationError('starts with a') 
def validation_forl_len(data):
    if len(data)<5:
        raise forms.ValidationError('len is < 5') 
    


                               
class SchoolForm(forms.Form): 
    Sname=forms.CharField(validators=[validation_for_a,validators.MinLengthValidator(4)])
    Sprincipal=forms.CharField(validators=[validation_forl_len])
    Slocation=forms.CharField()  
    email=forms.EmailField()
    reenteremail=forms.EmailField() 
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput) 

    def clean_botcather(self):
       b=self.cleaned_data['clean_botcather'] 
       if len(b)>0 :
          raise forms.ValidationError('BOT')
