from django.db import models
from schools.models import School, Season

class Level(models.Model):
    level = models.CharField(max_length=150)
    level_slug =  models.SlugField()
    def get_absolute_url(self):
        return "/levels/%s/" %self.slug
    def __unicode__(self):
        return self.level    

class Year(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        (u'FR', u'Freshman'),
        (u'SO', u'Sophomore'),
        (u'JR', u'Junior'),
        (u'SR', u'Senior'),
        (u'AL', u'Alumni'),
    )
    year = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    def __unicode__(self):
        return self.year 

class Rider(models.Model):
    name = models.CharField(max_length=200)
    name_slug = models.SlugField()
    hometown = models.CharField(max_length=200)
    def get_absolute_url(self):
        return "/rider/%i/" % self.id
    def __unicode__(self):
        return self.name

class RiderSeason(models.Model):
    rider = models.ForeignKey(Rider)
    season = models.ForeignKey(Season)
    school = models.ForeignKey(School)
    year = models.ForeignKey(Year)
    level = models.ManyToManyField(Level)
    points = models.IntegerField()
    def __unicode__(self):
        return "%s: %s" % (self.rider.name, self.season.season_name)

class Photo(models.Model):
    photo = models.ImageField(upload_to='photo')
    caption = models.TextField(blank=True, null=True)
    riders_in_photo = models.ManyToManyField(Season, blank=True, null=True)
    def __unicode__(self):
        return self.photo
