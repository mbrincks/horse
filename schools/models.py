from django.db import models

class Season(models.Model):
    season_name = models.CharField(max_length=255)
    season_name_slug = models.SlugField()
    def __unicode__(self):
        return self.season_name

class School(models.Model):
    school = models.CharField(max_length=255)
    school_slug = models.SlugField()
    school_abbreviation = models.CharField(max_length=10)
    def get_absolute_url(self):
        return "/schools/%s/" % self.slug
    def __unicode__(self):
        return self.school
