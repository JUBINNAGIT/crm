#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class MemberType(models.Model):
    uid = models.CharField(max_length=20, blank=False)
    group = models.CharField(max_length=50, blank=False)
    fallow = models.CharField(max_length=20, blank=False)
    utype = models.CharField(max_length=20, blank=True)
    memo = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    class Meta:
        ordering = ('utype', 'group')