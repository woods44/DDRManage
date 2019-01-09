from django.test import TestCase
from ddr_music_view.models import Music


class DDRMusicModelTests(TestCase):
    def test_save_music_attribute(self):
        music = Music()
        name = "Test"
        artist = "TAG"
        min_bpm = 100
        max_bpm = 300
        version = "X3"

        music.name = name
        music.artist = artist
        music.max_bpm = max_bpm
        music.min_bpm = min_bpm
        music.version = version
        music.save()
        test_musics = Music.objects.all()
        test_music = test_musics[0]

        self.assertEqual(test_music.name, name)
        self.assertEqual(test_music.artist, artist)
        self.assertEqual(test_music.min_bpm, min_bpm)
        self.assertEqual(test_music.max_bpm, max_bpm)
        self.assertEqual(test_music.version, version)
        self.assertTrue(test_music.max_bpm >= test_music.min_bpm)
