from .models import Post
from django.forms import ModelForm
from django import forms
from django.forms.widgets import TextInput, Textarea, Select ,FileInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','content','status','image']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'post-title'}),
            'slug': TextInput(attrs={'class': 'form-control form-control-sm', 'id': 'post-slug'}),
            'content': Textarea(attrs={'class': 'form-control form-control-sm', 'id': 'post-content'}),
            'status': Select(attrs={'class': 'form-control form-control-sm', 'id': 'post-status'}),
            'image': FileInput(attrs={'class': 'form-control-file form-control-sm', 'id': 'post-image'}),
        }