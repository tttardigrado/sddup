from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.fields import RichTextField


class LegalIndex(Page):
    subpage_types = ["LegalPage"]
    templates = "templates/legal/legal_index.html"

    def get_context(self, request, *args, **kwargs):
        # Get the default context so that no context variable is lost
        context = super().get_context(request, *args, **kwargs)

        # Get all posts, paginate them in groups of 12 and update the context
        context["docs"] = super().get_children()\
            .live().order_by("-first_published_at")

        return context


class LegalPage(Page):
    templates = "templates/legal/legal_page.html"

    text = RichTextField(
        verbose_name="Conteúdo",
        features=["h3", "h4", "bold", "italic", "link", "ol"],
    )

    content_panels = Page.content_panels + [
        FieldPanel("text"),
    ]
