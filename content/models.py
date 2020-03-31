from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from pages.models import Page


class Episode(models.Model):
    """Relevant episode information. This is specific to soundcloud-based
        podcasts but that can obviously be changed for the medium."""
    episode_number = models.IntegerField(default=0)
    episode_title = models.CharField(
        max_length=300,
        help_text="Leave out the episode number.")
    embed = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        help_text="On Soundcloud, click on Share, then Embed, " +
            "then select the rightmost option from the three squares " +
            "on the top, then copy the contents of the box labeled 'Code' " +
            "and paste here.")
    patreon_episode = models.BooleanField(
        default=False,
        help_text="Select if this is a patreon episode")
    patreon_link = models.URLField(
        max_length=300,
        null=True,
        blank=True,
        help_text="If this is a Patreon episode, use the location of the " +
            "specific episode page. e.g. " +
            "'https://www.patreon.com/posts/episode-146-neat-thing'.")
    episode_description = models.TextField(
        help_text="Do not include citations from the episode " +
            "desctiption. Use the 'add citation' functionality for that. " +
            "HTML is available, but please only use for links and basic styling.")
    show_topics = models.BooleanField(
        default=False,
        help_text="Select this to display topics linked to this episode.")
    slug = models.SlugField(
        max_length=300,
        null=False,
        unique=True)

    class Meta:
        ordering = ["-episode_number"]

    def __str__(self):
        """Return episode title"""
        return str(self.episode_number) + "-" + self.episode_title

    def get_absolute_url(self):
        """Redirect to newly created episode page"""
        return reverse('episode', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.episode_number) + "-" + self.episode_title)
        return super().save(*args, **kwargs)


class EpisodeCitation(models.Model):
    """Citation model specific to episodes"""
    episode = models.ForeignKey(
        Episode,
        on_delete=models.CASCADE,
        related_name="citations")
    citation_title = models.CharField(
        max_length=500,
        help_text="e.g.: Neat Thing Happened, Study Finds")
    citation_publication = models.CharField(
        max_length=100,
        help_text="Source, e.g. 'New York Times'.")
    citation_link = models.URLField(
        max_length=500,
        help_text="")
    archive_link_available = models.BooleanField(
        default=False,
        help_text="Select to display a backup link from the internet archive.")
    archive_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="A link from the web archive to supplement original.")
    citation_description = models.TextField(
        help_text="One to two sentence overview of citation contents.")

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.citation_title


class Topic(models.Model):
    """Model for topic description pages. Use net worth if describing
        a rich person."""
    topic_name = models.CharField(
        max_length=300)
    net_worth = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        help_text="Number in billions up to two decimal points.")
    net_worth_source = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Short name of source of net worth, e.g. 'Forbes'.")
    net_worth_source_date = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Year or month and year net worth was reported, e.g. '2020'" +
            " or 'March 2020'.")
    net_worth_source_link = models.URLField(
        blank=True,
        null=True,
        help_text="URL of net worth source, e.g. " +
            "'https://www.forbes.com/profile/jeff-bezos/'")
    topic_bio = models.TextField(
        help_text="Do not include citations here. Add those after the page is created." +
        "HTML is available, but please only use for links and basic styling.")
    topic_pic_filename = models.CharField(
        max_length=200,
        default="grubman.png",
        help_text="Filename of image uploaded to AWS topics folder, " +
            "e.g. 'epstein.png'.")
    topic_pic_caption = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Image attribution and/or caption.")
    slug = models.SlugField(
        max_length=300,
        null=False,
        unique=True)
    episode = models.ManyToManyField(
        Episode,
        blank=True,
        related_name='topics',
        through='EpisodeTopic')

    class Meta:
        ordering = ["-net_worth"]

    def __str__(self):
        """Return episode title"""
        return self.topic_name

    def get_absolute_url(self):
        """Redirect to newly created topic page"""
        return reverse('topic', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.topic_name))
        return super().save(*args, **kwargs)


class TopicCitation(models.Model):
    """Citation model specific to topics"""
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="citations")
    citation_title = models.CharField(
        max_length=500,
        help_text="e.g.: Neat Thing Happened, Study Finds")
    citation_publication = models.CharField(
        max_length=100,
        help_text="Source, e.g. 'New York Times'.")
    citation_link = models.URLField(
        max_length=500,
        help_text="Article link.")
    archive_link_available = models.BooleanField(
        default=False,
        help_text="Select to display a backup link from the internet archive.")
    archive_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="A link from the web archive to supplement original.")
    citation_description = models.TextField(
        help_text="One to two sentence overview of citation contents.")

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return self.citation_title


class EpisodeTopic(models.Model):
    """Intermediate model linking episodes and topics"""
    episode = models.ForeignKey(
        Episode,
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='episodes')
