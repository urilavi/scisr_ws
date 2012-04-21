#!/usr/bin/env python
from django.contrib import admin
from scisr_ws.events.models import Event, Link, Tickets

class LinkInline(admin.TabularInline):
    model  = Link
    extra  = 2

class TicketsInLine(admin.TabularInline):
    model = Tickets
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [LinkInline, TicketsInLine]

admin.site.register(Event, EventAdmin)