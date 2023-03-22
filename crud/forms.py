from re import I
from django import forms
from crud.models import Gaurav


class UserForm(forms.ModelForm):
    class Meta:
        model = Gaurav
        fields = "__all__"
        widget = {
        
        'uname':forms.TextInput(attrs={'class':'form-control'}),
        'uemail':forms.EmailInput(attrs={'class':'form-control'}),
        'upassword':forms.TextInput(attrs={'class':'form-control'}),
        }