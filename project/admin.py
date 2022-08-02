from django.contrib import admin
from .models import Song, Singer, Album, Tag, Playlist

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "when_born", "where_born", "image")
    search_fields = ("first_name", "last_name",)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("singer", "title", "cover", "tag")
    search_fields = ("title",)
    list_filter = ("tag",)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("album", "title", "image", "audio", "tag")
    search_fields = ("album__title", "title", "album__singer__first_name")
    list_filter = ("tag",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("name", "song")

# Register your models here.
