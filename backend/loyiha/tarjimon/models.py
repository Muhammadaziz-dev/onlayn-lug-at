from django.db import models

class Lugat(models.Model):

    ingilizcha = models.CharField('Ingilizcha', max_length=128)
    uzbekcha = models.CharField('O`zbekcha', max_length=128)
