from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import (Episode,
                    EpisodeCitation,
                    Topic,
                    TopicCitation,
                    EpisodeTopic, )
from .forms import EpisodeForm, TopicForm


class EpisodeDetailView(DetailView):
    """Show detail for individual episodes"""
    model = Episode
    template_name = 'episodes/episode_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EpisodeDetailView, self).get_context_data(*args, **kwargs)
        context['episodes'] = Episode.objects.all()
        context['topics'] = Topic.objects.all()
        return context


class EpisodeCreateView(LoginRequiredMixin, CreateView):
    """Add episode"""
    model = Episode
    template_name = 'episodes/add_episode.html'
    login_url = 'login'
    form_class = EpisodeForm


class EpisodeUpdateView(LoginRequiredMixin, UpdateView):
    """Update episode info"""
    model = Episode
    template_name = 'episodes/update_episode.html'
    login_url = 'login'
    form_class = EpisodeForm


class EpisodeCitationCreateView(LoginRequiredMixin, CreateView):
    """Add episode citations"""
    model = EpisodeCitation
    template_name = 'citations/add_citation.html'
    login_url = 'login'
    success_url = reverse_lazy('episode_list')
    fields = [
        'episode',
        'citation_title',
        'citation_publication',
        'citation_link',
        'archive_link_available',
        'archive_link',
        'citation_description', ]


class EpisodeCitationUpdateView(LoginRequiredMixin, UpdateView):
    """Update episode citations"""
    model = EpisodeCitation
    template_name = 'citations/update_citation.html'
    login_url = 'login'
    success_url = reverse_lazy('episode_list')
    fields = [
        'episode',
        'citation_title',
        'citation_publication',
        'citation_link',
        'citation_description', ]


class TopicDetailView(DetailView):
    """Show detail for individual topic"""
    model = Topic
    template_name = 'topics/topic_detail.html'


class TopicCreateView(LoginRequiredMixin, CreateView):
    """Add topic"""
    model = Topic
    template_name = 'topics/add_topic.html'
    login_url = 'login'
    form_class = TopicForm


class TopicUpdateView(LoginRequiredMixin, UpdateView):
    """Update topic info"""
    model = Topic
    template_name = 'topics/update_topic.html'
    login_url = 'login'
    form_class = TopicForm


class TopicCitationCreateView(LoginRequiredMixin, CreateView):
    """Add episode citations"""
    model = TopicCitation
    template_name = 'citations/add_citation.html'
    login_url = 'login'
    success_url = reverse_lazy('topic_list')
    fields = [
        'topic',
        'citation_title',
        'citation_publication',
        'citation_link',
        'archive_link_available',
        'archive_link',
        'citation_description', ]


class TopicCitationUpdateView(LoginRequiredMixin, UpdateView):
    """Update episode citations"""
    model = TopicCitation
    template_name = 'citations/update_citation.html'
    login_url = 'login'
    success_url = reverse_lazy('topic_list')
    fields = [
        'topic',
        'citation_title',
        'citation_publication',
        'citation_link',
        'archive_link_available',
        'archive_link',
        'citation_description', ]
