from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BoardMember(blocks.StructBlock):
    name = blocks.CharBlock(required=True, verbose_name="Nome")
    position = blocks.CharBlock(required=True, verbose_name="Cargo")
    image = ImageChooserBlock(required=True, verbose_name="Fotografia")

    class Meta:
        template = "board/board_member.html"
        label = "Membro"
        icon = "edit"
