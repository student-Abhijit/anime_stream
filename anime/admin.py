from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Anime, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1

class AnimeAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre']
    search_fields = ['title', 'genre']
    inlines = [EpisodeInline]

admin.site.register(Anime, AnimeAdmin)
