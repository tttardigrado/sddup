from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from . import blocks


class HomePage(Page):
    templates = "templates/home/home_page.html"
    max_count = 1

    # Banner to be presented at the top of the page
    banner_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name="Título",
    )
    banner_subtitle = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        verbose_name="Sub-Título",
    )
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content = StreamField(
        [("home_content", blocks.HomeContent())],
        null=True,
        blank=True,
        use_json_field=False,
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        FieldPanel("content"),
    ]
