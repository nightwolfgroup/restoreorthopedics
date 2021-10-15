from django.db import models
from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag


@register_snippet
class Testimonial(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=True,
    )
    quote = models.TextField(
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.quote


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
