from django.db import models


class Music(models.Model):
    name = models.CharField('楽曲名', max_length=255)
    artist = models.CharField('作者', max_length=255)
    max_bpm = models.IntegerField(default=0)
    min_bpm = models.IntegerField(default=0)
    version = models.CharField('バージョン', max_length=255)

