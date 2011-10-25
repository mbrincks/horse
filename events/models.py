from django.db import models

class School(models.Model):
    school = models.CharField(max_length=255)
    school_slug = models.SlugField()
    school_abbreviation = models.CharField(max_length=10)
    def __unicode__(self):
        return self.school

class EventType(models.Model):
    EVENT_TYPE_CHOICES = (
        (u'HJ', u'Hunt_Seat'),
        (u'WR', u'Western'),
    )
    event_type = models.CharField(max_length=2, choices=EVENT_TYPE_CHOICES)
    def __unicode__(self):
        return self.eventtype

class Photo(models.Model):
    image = models.ImageField(upload_to='photo')
    caption = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return self.photo

class Event(models.Model):
    host_school = models.ForeignKey(School)
    location = models.CharField(max_length=200)
    event_type = models.ForeignKey(EventType)
    date = models.DateTimeField()
    high_point_rider = models.CharField(max_length=200)
    reserve_rider = models.CharField(max_length=200)
    high_point_team = models.ForeignKey(School, related_name="high_point_school")
    reserve_team = models.ForeignKey(School, related_name="reserve_team_school")
    photo = models.ForeignKey(Photo)
