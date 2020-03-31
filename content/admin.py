from django.contrib import admin

from .models import Episode, EpisodeCitation, Topic, TopicCitation


class EpisodeCitationInline(admin.TabularInline):
    model = EpisodeCitation


class EpisodeAdmin(admin.ModelAdmin):
    inlines = [
        EpisodeCitationInline,
    ]
    list_display = ( 'episode_number', 'episode_title', )
    prepopulated_fields = {'slug': ('episode_title',)}


class TopicCitationInline(admin.TabularInline):
    model = TopicCitation


class TopicAdmin(admin.ModelAdmin):
    inlines = [
        TopicCitationInline,
    ]
    list_display = ( 'topic_name', 'net_worth', )
    prepopulated_fields = {'slug': ('topic_name',)}


admin.site.register(Episode, EpisodeAdmin)
admin.site.register(EpisodeCitation)
admin.site.register(Topic, TopicAdmin)
admin.site.register(TopicCitation)
