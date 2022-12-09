from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])



class Blog(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    class Meta:
        ordering = ['created']
