from django.db import models
from schools.models import School, Season
from riders.models import RiderSeason

class EventType(models.Model):
    EVENT_TYPE_CHOICES = (
        (u'HJ', u'Hunt_Seat'),
        (u'WR', u'Western'),
    )
    event_type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES)
    def get_absolute_url(self):
        return "/eventtype/%i/" % self.id
    def __unicode__(self):
        return self.event_type

class Photo(models.Model):
    image = models.ImageField(upload_to='static/photo')
    caption = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return "%i" % self.id

class Event(models.Model):
    season = models.ForeignKey(Season, blank=True, null=True)
    host_school = models.ForeignKey(School)
    location = models.CharField(max_length=200)
    event_type = models.ForeignKey(EventType)
    date = models.DateTimeField()
    high_point_rider = models.ForeignKey(RiderSeason, related_name="high_point_set", blank=True, null=True)
    reserve_rider = models.ForeignKey(RiderSeason, related_name="reserve_set", blank=True, null=True)
    high_point_team = models.ForeignKey(School, related_name="high_point_school", blank=True, null=True)
    reserve_team = models.ForeignKey(School, related_name="reserve_team_school", blank=True, null=True)
    participating_teams = models.ManyToManyField(School, blank=True, null=True, related_name="participating_school_set")
    participating_riders = models.ManyToManyField(RiderSeason, blank=True, null=True, related_name="participating_rider_set")
    photo = models.ForeignKey(Photo, blank=True, null=True)
    def get_absolute_url(self):
        return "/event/%i/" % self.id
    def __unicode__(self):
        return "%s at %s" % (self.event_type.event_type, self.host_school.school)
