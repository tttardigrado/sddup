from datetime import datetime

from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class PostIndex(Page):
    subpage_types = ["BlogPost"]
    templates = "templates/blog/post_index.html"

    def get_context(self, request, *args, **kwargs):
        # Get the default context so that no context variable is lost
        context = super().get_context(request, *args, **kwargs)

        # Get all posts, paginate them in groups of 12 and update the context
        context["posts"] = self.paginate(request, 2)

        return context

    def paginate(self, request, posts_per_page):
        all_posts = super().get_children()\
            .live().order_by("-first_published_at")
        paginator = Paginator(all_posts, posts_per_page)
        page = request.GET.get("page")

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return posts


class BlogPost(Page):
    subpage_types = []
    templates = "templates/blog/blog_post.html"

    # Date the post has been posted at
    #   so that it can be sorted by date
    date = models.DateField(
        default=datetime.now,
        null=True,
        verbose_name="Data",
    )

    # Thumbnail image
    thumbnail = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    # Introduction to the article
    teaser = RichTextField(
        features=["bold", "italic", "link"],
        null=True,
    )

    # Rest of the content of the article
    body = RichTextField(null=True)

    # Admin panels
    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("thumbnail"),
        FieldPanel("teaser"),
        FieldPanel("body"),
    ]

    # Searchable fields
    search_fields = Page.search_fields + [
        index.SearchField("title"),
        index.SearchField("teaser"),
        index.SearchField("body"),
    ]
