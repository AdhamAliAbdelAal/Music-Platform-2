from django.contrib import admin
from .models import Album
from django import forms


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('artist','name','cost','release_time','is_approved')
        help_texts = {'is_approved': "Approve the album if its name is not explicit", }


class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    readonly_fields = ('creation_time',)
    list_display=('name','is_approved')


admin.site.register(Album, AlbumAdmin)