from events.models import Event
from django.shortcuts import render_to_response
from django.http import HttpResponsePermanentRedirect

def next_event(request):
    nextEvent = Event.objects.all().order_by('-number')[0]
    return render_to_response('next_event.html', {'event' : nextEvent})

def previous_events(request):
    previousEvents = Event.objects.all().order_by('-number')
    return render_to_response('previous_events.html', {'previousEvents' : previousEvents})
    
def about(request):
    return render_to_response('about.html')

def feedburner_events(request):
    if request.META['HTTP_USER_AGENT'].startswith('FeedBurner'):
        return EventsFeed(request)
    else:
        return HttpResponsePermanentRedirect('http://feeds.feedburner.com/SCISR-Events')
