from django import forms
from django.forms import ModelForm
from albums.models import Album

class AlbumForm(ModelForm):
    class Meta:
        model=Album
        fields = ('artist','name','cost','release_time','is_approved')
        widgets={
            'release_time':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }