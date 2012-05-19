from django.conf.urls.defaults import patterns, include, url, handler404
from events.feeds.events_feed import EventsFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('events.views',
    url(r'^$', 'next_event', name='nextEvent'),
    url(r'^events/$', 'previous_events', name='previousEvents'),
    url(r'^events/rss/$', 'feedburner_events'),
    url(r'^about/$', 'about', name='about'),
    # url(r'^events/rss/$', EventsFeed()),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('',    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

