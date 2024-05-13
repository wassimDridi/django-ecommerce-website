from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import TextInput, Textarea, Select ,FileInput

from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'post-title'}),
            'last_name': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'post-slug'}),
            'email': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'post-slug'}),
        }


class UserRegistrationForm(UserCreationForm):
 first_name = forms.CharField(label='Prénom')
 last_name = forms.CharField(label='Nom')
 email = forms.EmailField(label='Adresse e-mail')
 
class Meta(UserCreationForm.Meta):
 model = User
 fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')