from django.db import models

class Page(models.Model):
    """Descriptions for a discrete number of landing pages"""
    page_type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(
        help_text = "HTML is available, but please only use for links and basic styling.")
