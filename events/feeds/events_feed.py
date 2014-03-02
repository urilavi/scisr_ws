from django.contrib.syndication.views import Feed
from events.models import Event

class EventsFeed(Feed):
    title               = 'Software Craftsmanship In Israel Events Feed'
    link                = '/events/rss/'
    description         = 'Software Craftsmanship In Israel Events Feed'

    def items(self):
        return Event.objects.all().order_by('-number')[:5]

    def item_title(self, item):
        return 'Meeting {0}: {1}'.format(item.number, item.title)

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return '{0}{1}'.format('http://israel.softwarecraftsmanship.org/events/#', item.number)

