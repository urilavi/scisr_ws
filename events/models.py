from django.db import models

# Create your models here.
class Event(models.Model):
    '''
    Event class represents Software Craftsmanship Events.
    '''
    number      = models.IntegerField()
    title       = models.CharField(max_length=200)
    description = models.TextField()
    schedule    = models.TextField()
    epilogue    = models.CharField(max_length=200, blank=True)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
    location    = models.CharField(max_length=300)

    def __unicode__(self):
        return 'Event Number: {0}'.format(self.number)
        
class Link(models.Model):
    event       = models.ForeignKey(Event)
    uri         = models.URLField(max_length=300)
    description = models.CharField(max_length=300)
    
    def __unicode__(self):
        return 'Event Number: {0}, link to {1}'.format(self.event.number, self.uri)

class Tickets(models.Model):
    event       = models.OneToOneField(Event)
    data        = models.TextField()

    def __unicode__(self):
        return 'Event Number: {0} Tickets details'.format(self.event.number)