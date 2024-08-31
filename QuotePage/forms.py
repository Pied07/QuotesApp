from django import forms
from .models import Quote,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['name','title','quote_body','photo','caption','fontfamily','fontcolor','fontsize']
        widgets = {
            'fontcolor': forms.TextInput(attrs={
                'type': 'color'
            }),
            'fontsize': forms.NumberInput(attrs={
                'type': 'range',
                'min': '10',
                'max': '70',
                'step': '1',
                'value': '20'
            })
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class' : 'form-control',
                'rows': 3,
                'placeholder' : ' Enter a new Comment!',
            })
        }
