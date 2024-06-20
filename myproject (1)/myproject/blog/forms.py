from django import forms
from django.forms import fields, widgets
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control custom-txt','cols':'40','rows':'3'}), label='')
    class Meta:
        model = Comment
        fields = ['body',]

# forms.py

class CoinGameForm(forms.Form):
    FLIP_CHOICES = [
        (0, 'Keep'),
        (1, 'Flip')
    ]

    PILE_CHOICES = [
        (0, 'Pile 1'),
        (1, 'Pile 2')
    ]

    flips = forms.ChoiceField(choices=FLIP_CHOICES, widget=forms.RadioSelect, label="Flip")
    piles = forms.ChoiceField(choices=PILE_CHOICES, widget=forms.RadioSelect, label="Pile")
