from django.urls import path

from .views import (
    EpisodeCreateView,
    EpisodeUpdateView,
    EpisodeCitationCreateView,
    EpisodeCitationUpdateView,
    TopicDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicCitationCreateView,
    TopicCitationUpdateView,
    )

urlpatterns = [
    # Episodes
    path('new_episode/',
        EpisodeCreateView.as_view(),
        name='add_episode'),

    path('new_episode_citation/',
        EpisodeCitationCreateView.as_view(),
        name='add_episode_citation'),

    path('update_episode_citation/<int:pk>',
        EpisodeCitationUpdateView.as_view(),
        name='update_episode_citation'),

    path('episode/<slug:slug>/update/',
        EpisodeUpdateView.as_view(),
        name='update_episode'),

    # Topics
    path('new_topic/',
        TopicCreateView.as_view(),
        name='add_topic'),

    path('new_topic_citation/',
        TopicCitationCreateView.as_view(),
        name='add_topic_citation'),

    path('update_topic_citation/<int:pk>',
        TopicCitationUpdateView.as_view(),
        name='update_topic_citation'),

    path('topic/<slug:slug>/update/',
        TopicUpdateView.as_view(),
        name='update_topic'),
]
