from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from . import blocks


class BoardPage(Page):
    """Page that shows the different memebers of organization"""

    template = "board/board_page.html"

    board = StreamField(
        [("board", blocks.BoardMember())],
        null=True,
        blank=True,
        use_json_field=False,
        verbose_name="Direção",
    )
    general_assembly = StreamField(
        [("general_assembly", blocks.BoardMember())],
        null=True,
        blank=True,
        use_json_field=False,
        verbose_name="Mesa da Assembleia Geral",
    )
    auditing = StreamField(
        [("auditing", blocks.BoardMember())],
        null=True,
        blank=True,
        use_json_field=False,
        verbose_name="Conselho Fiscal",
    )

    content_panels = Page.content_panels + [
        FieldPanel("board"),
        FieldPanel("general_assembly"),
        FieldPanel("auditing"),
    ]

    class Meta:
        verbose_name = "Orgãos Sociais"
        verbose_name_plural = "Mandatos"
