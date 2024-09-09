from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import PreviewableMixin
from wagtail.snippets.models import register_snippet


@register_snippet
class MediaLinks(PreviewableMixin, models.Model):
    """Snippet to register social media sharing options for the footer
    Every MediaLink has an icon and an url that will appear on the footer
    Pressing the icon will redirect the user to the provided url
    """

    # Social media icon choices
    # for bootstrap icons - user-friendly version
    CHOICE = (
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("messenger", "Messenger"),
        ("twitter", "Twitter"),
        ("pinterest", "Pinterest"),
        ("whatsapp", "WhatsApp"),
        ("linkedin", "LinkedIn"),
        ("youtube", "Youtube"),
        ("tiktok", "TikTok"),
        ("reddit", "Reddit"),
        ("discord", "Discord"),
        ("telegram", "Telegram"),
        ("medium", "Medium"),
    )
    icon_name = models.CharField(
        max_length=63, choices=CHOICE, verbose_name="Nome do Icon"
    )

    # Url the user should be sent to when the icon is pressed
    url = models.URLField()

    # Admin panels
    panels = [
        FieldPanel("icon_name"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.icon_name

    def get_preview_template(self, request, mode_name):
        return "core/previews/footer_preview.html"

    class Meta:
        verbose_name_plural = "redes sociais"
        verbose_name = "rede social"
        ordering = ["icon_name"]


@register_snippet
class Contact(PreviewableMixin, models.Model):
    """Snippet to register contact information for the footer
    Every contact will appear as a paragraph under the "Contact" section
    """

    # Contact title for the contact page
    title = models.CharField(
        max_length=255,
        verbose_name="Título do Contacto",
    )

    # Kind of contact (E-mail, phone)
    # Appears before the contact itself
    CHOICE = (
        ("phone", "Telemóvel"),
        ("envelope-fill", "E-Mail"),
        ("house-fill", "Morada"),
    )
    kind = models.CharField(
        max_length=63,
        choices=CHOICE,
        verbose_name="Tipo de contacto",
    )

    # Contact information that will be shown under the "Contact" section
    text = models.CharField(
        max_length=255,
        verbose_name="Informação do Contacto",
    )

    # Should be shown in the footer ot just in the full contact page
    show_in_footer = models.BooleanField(
        verbose_name="Mostrar no Footer",
        default=True,
    )

    order = models.IntegerField(
        verbose_name="Ordem",
        default=0,
    )

    # Admin panels
    panels = [
        FieldPanel("title"),
        FieldPanel("kind"),
        FieldPanel("text"),
        FieldPanel("show_in_footer"),
        FieldPanel("order"),
    ]

    def __str__(self):
        return self.title

    def get_preview_template(self, request, mode_name):
        return "core/previews/footer_preview.html"

    class Meta:
        verbose_name_plural = "contactos"
        verbose_name = "contacto"
        ordering = ["order", "title", "kind", "text"]


@register_snippet
class Sponsor(PreviewableMixin, models.Model):
    """Snippet to register a sponsor information for the footer
    Every sponsor's logo will appear as a list item under the "Sponsor" section
    """

    logo = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Logo do Patrocinador",
    )

    # Contact information that will be shown under the "Contact" section
    name = models.CharField(
        max_length=255,
        verbose_name="Nome do Patrocinador",
    )

    # Admin panels
    panels = [FieldPanel("logo"), FieldPanel("name")]

    def __str__(self):
        return self.name

    def get_preview_template(self, request, mode_name):
        return "core/previews/footer_preview.html"

    class Meta:
        verbose_name_plural = "Patrocinadores"
        verbose_name = "Patrocinador"
        ordering = ["name"]


@register_snippet
class Event(models.Model):
    """Snippet to register a new event in the organization's calendar"""

    # Basic info about the event
    name = models.CharField(max_length=100, verbose_name="Nome do Evento")
    location = models.CharField(max_length=100, verbose_name="Local do Evento")
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(verbose_name="Data de Fim")
    hour = models.TimeField(
        blank=True,
        null=True,
        verbose_name="Horário",
    )
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link",
    )

    # Admin panels
    panels = [
        FieldPanel("name"),
        FieldPanel("location"),
        FieldPanel("start_date"),
        FieldPanel("end_date"),
        FieldPanel("hour"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Eventos"
        verbose_name = "Evento"
        ordering = ["start_date", "name"]
