from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=100)
    ans_type = models.BooleanField(default=False)
    answer = models.CharField(max_length=400)
