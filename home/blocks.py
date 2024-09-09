from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomeContent(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock(required=True)
    image_left = blocks.BooleanBlock(required=False, default=False)

    # button
    btn_text = blocks.CharBlock(required=False)
    btn_url = blocks.CharBlock(required=False)
    btn_page = blocks.PageChooserBlock(required=False)

    class Meta:
        template = "home/home_block.html"
        label = "Panels"
        icon = "edit"
