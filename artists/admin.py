from django.contrib import admin
from artists.models import Artist
from albums.models import Album

class AlbumInline(admin.TabularInline):
    model=Album

class ArtistAdmin(admin.ModelAdmin):
    inlines=[AlbumInline]
    list_display=['stage_name','approved_albums']
    def approved_albums(self, obj):
        return obj.album_set.filter(is_approved=True).count()
    approved_albums.short_description='Number of apporoved albums'



admin.site.register(Artist,ArtistAdmin)