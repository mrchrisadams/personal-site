from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from wagtailmarkdown.fields import MarkdownField, MarkdownPanel

class HomePage(Page):
    pass

class BlogPost(Page):
    date = models.DateField("Post date")
    body = MarkdownField()

BlogPost.content_panels = [
    FieldPanel("title", classname="full title"),
    FieldPanel('date'),
    MarkdownPanel("body"),
]
