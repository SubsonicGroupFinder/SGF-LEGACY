from django import forms
from django.forms import fields, widgets
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm

class PostCreation(forms.ModelForm):
    title = forms.CharField(widget='Title', widgets=forms.TextInput)
    
    class Meta:
        model = User
        fields = ('title', 'description', 'createdOn', 'lastEdited', 'game', 'platform', 'body', 'tags')
    
    class clean_title(self):
        title = self.cleaned_data.get('title')
        
        