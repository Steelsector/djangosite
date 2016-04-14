from __future__ import unicode_literals

from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255)
    rate = models.IntegerField()


class Projects(models.Model):
    name = models.CharField(max_length=255)
    technologies = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='projects')
