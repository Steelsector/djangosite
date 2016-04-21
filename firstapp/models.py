from __future__ import unicode_literals

from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255)
    rate = models.IntegerField()

    def __unicode__(self):
        return '%s (%s)' % (self.name, self.rate)


class Project(models.Model):
    name = models.CharField(max_length=255)
    technologies = models.ManyToManyField(Skill)
    photo = models.ImageField(upload_to='projects')
    linkto = models.URLField(max_length=200, default='SOME STRING')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
