from django import forms
from django.forms import fields, widgets
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm

class PostCreation(forms.ModelForm):
    title = forms.CharField(widget='Title', widgets=forms.TextInput)
    
    class Meta:
        model = User
        fields = ('title', 'description', 'createdOn', 'lastEdited', 'game', 'platform', 'body', 'tags')
        
        def clean_title(self):
            title = self.cleaned_data['title']
            return title
        
        def clean_description(self):
            description = self.cleaned_data['description']
            return description
        
        def clean_platform(self):
            platform = self.cleaned_data['platform']
            return platform

        def clean_game(self):
            game = self.cleaned_data['game']
            return game
        
        def clean_body(self):
            body = self.cleaned_data['body']
            return body
        
        def clean_tags(self):
            tags = self.cleaned_data['tags']
            return tags