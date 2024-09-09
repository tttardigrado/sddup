from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Book(models.Model):
    """Snippet to register a new book in the organization's library"""

    # Basic info about the book
    title = models.CharField(max_length=100, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    url = models.URLField(verbose_name="Link do Goodreeds")
    language = models.CharField(max_length=20, verbose_name="Língua do Livro")

    # Availability info
    landed_to = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Requisitado por",
    )
    landed_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Requisitado no dia",
    )

    # Admin panels
    panels = [
        FieldPanel("title"),
        FieldPanel("author"),
        FieldPanel("url"),
        FieldPanel("language"),
        MultiFieldPanel([
            FieldPanel("landed_to"),
            FieldPanel("landed_date")
        ], "Requisição")
    ]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Livros"
        verbose_name = "Livro"
        ordering = ["title"]
