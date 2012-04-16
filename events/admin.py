#!/usr/bin/env python
from django.contrib import admin
from scisr_ws.events.models import Event, Link

class LinkInline(admin.TabularInline):
    model  = Link
    extra  = 2

class EventAdmin(admin.ModelAdmin):
    inlines = [LinkInline]

admin.site.register(Event, EventAdmin)