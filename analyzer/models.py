from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    tf = models.IntegerField(verbose_name='tf')
    idf = models.IntegerField(verbose_name='idf')
