from django.shortcuts import render, get_object_or_404
from .models import Anime, Episode

def home(request):
    animes = Anime.objects.all()
    return render(request, 'home.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'anime_detail.html', {'anime': anime})

def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id)
    return render(request, 'episode_detail.html', {'episode': episode})
