# from django.test import TestCase

# # Create your tests here.
# from django.test import TestCase
# from .models import Anime, Episode

# class AnimeTestCase(TestCase):
#     def setUp(self):
#         anime = Anime.objects.create(
#             title="Naruto",
#             description="A story about a ninja",
#             genre="Action"
#         )
#         Episode.objects.create(
#             anime=anime,
#             title="Enter Naruto",
#             episode_number=1,
#             video_url="https://example.com/video.mp4"
#         )

#     def test_anime_created(self):
#         anime = Anime.objects.get(title="Naruto")
#         self.assertEqual(anime.genre, "Action")

#     def test_episode_link(self):
#         episode = Episode.objects.get(episode_number=1)
#         self.assertTrue("video.mp4" in episode.video_url)
