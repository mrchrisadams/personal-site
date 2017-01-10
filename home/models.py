from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks


from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

from wagtailmarkdown.fields import MarkdownField, MarkdownPanel, MarkdownBlock

from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
class HomePage(Page):
    pass

class BlogPost(Page):
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
        ('markdown', MarkdownBlock()),
    ])


BlogPost.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel('date'),
    StreamFieldPanel('body'),
]
