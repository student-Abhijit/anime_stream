from django.db import models

class Anime(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    episode_number = models.IntegerField()
    video_url = models.URLField(blank=True, null=True)  # Optional if you still want URL
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)  # New optional field

    def __str__(self):
        return f"{self.anime.title} - Episode {self.episode_number}"
