from django import template

from ..models import Contact, MediaLinks, Sponsor, Event

register = template.Library()


# Contact snippets tag
@register.inclusion_tag("snippets/contact.html", takes_context=True)
def contact(context):
    """Pass all Contact snippets to the contact tag as context
    so that it can be accessed and displayed as a list
    """
    return {
        "contacts": Contact.objects.all(),
        "request": context["request"],
    }


# Social Media snippets
@register.inclusion_tag("snippets/social_media.html", takes_context=True)
def social_media(context):
    """Pass all media link snippets to the social_media tag as context
    so that they can be displayed as a list of icons with links
    """
    return {
        "links": MediaLinks.objects.all(),
        "request": context["request"],
    }


# Sponsor snippets
@register.inclusion_tag("snippets/sponsor.html", takes_context=True)
def sponsor(context):
    """Pass all sponsor snippets to the sponsor tag as context
    so that they can be displayed as a list of images
    """
    return {
        "sponsors": Sponsor.objects.all(),
        "request": context["request"],
    }


# Event list table snippet
@register.inclusion_tag("snippets/next_events.html", takes_context=True)
def next_events(context):
    """Pass the next **num** events
    so that it can be displayed as a list
    """
    return {
        "events": Event.objects.all().order_by("start_date")[:5],
        "request": context["request"],
    }
