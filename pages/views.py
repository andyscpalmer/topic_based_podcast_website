from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView

from .models import Page
from content.models import Episode, Topic
from users.models import CustomUser


class HomePageView(TemplateView):
    """Create a home page."""
    template_name = 'home.html'

    def get_context_data(self, *args,  **kwargs):
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['home'] = Page.objects.get(page_type="Home")
        context['episode'] = Episode.objects.all()
        return context


class AboutPageView(TemplateView):
    """Create an about page."""
    template_name = 'about.html'

    def get_context_data(self, *args,  **kwargs):
        context = super(AboutPageView, self).get_context_data(*args, **kwargs)
        context['about'] = Page.objects.get(page_type="About")
        return context


class PodhostList(ListView):
    """Show the pod host list within the about page."""
    context_object_name = 'podhost_list'
    template_name = 'podhosts/podhost_list.html'
    queryset = CustomUser.objects.all()

    def get_context_data(self, *args,  **kwargs):
        context = super(PodhostList, self).get_context_data(*args, **kwargs)
        context['about'] = Page.objects.get(page_type="About")
        context['podhost'] = CustomUser.objects.all()
        return context


class EpisodeListView(ListView):
    """Pull list from Episode model and display on episodes page."""
    context_object_name = 'episode_list'
    template_name = 'episodes/episode_list.html'
    model = Episode
    paginate_by = 10

    def get_context_data(self, *args,  **kwargs):
        context = super(EpisodeListView, self).get_context_data(*args, **kwargs)
        context['episodes_page'] = Page.objects.get(page_type="Episodes")
        p = Paginator(Episode.objects.select_related().all(), self.paginate_by)
        context['episode_list'] = p.page(context['page_obj'].number)
        return context


class EpisodePageView(TemplateView):
    """Create the template for the episode list"""
    template_name = 'episodes.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EpisodePageView, self).get_context_data(*args, **kwargs)
        context['episodes_page'] = Page.objects.get(page_type='Episodes')
        return context


class TopicListView(ListView):
    """Pull list from Topic model and display on topic page."""
    context_object_name = 'topic_list'
    template_name = 'topics/topic_list.html'
    model = Topic
    paginate_by = 10

    def get_context_data(self, *args,  **kwargs):
        context = super(TopicListView, self).get_context_data(*args, **kwargs)
        context['topics_page'] = Page.objects.get(page_type="Topics")
        p = Paginator(Topic.objects.select_related().all(), self.paginate_by)
        context['topic_list'] = p.page(context['page_obj'].number)
        return context


class TopicPageView(TemplateView):
    """Create the template for the episode list"""
    template_name = 'topics.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TopicPageView, self).get_context_data(*args, **kwargs)
        context['topics_page'] = Page.objects.get(page_type='Topics')
        return context


class UpdatePageView(LoginRequiredMixin, UpdateView):
    """Update page descriptions for home, about, episodes, topics"""
    model = Page
    template_name = 'update_page.html'
    login_url = 'login'
    success_url = reverse_lazy('home')
    fields = [ 'title', 'content', ]


class SearchResultsListView(ListView):
    """Search for topics"""
    model = Topic, Episode
    context_object_name = 'results_list'
    template_name = 'search_results.html'
    #paginate_by = 3

    def get_queryset(self):
        '''Search topics and episodes excluding blank queries,
           single letter queries, and common words'''
        query = self.request.GET.get('q')
        if len(query) > 1:
            topics = Topic.objects.filter(
                Q(topic_name__icontains=query)
                #| Q(topic_bio__icontains=query)
                )
            if query.lower() != "the" and query.lower() != "feat" and query.lower() != "and":
                episodes = Episode.objects.filter(
                    Q(episode_title__icontains=query)
                    #| Q(episode_description__icontains=query)
                    )
            else:
                episodes = ()

            return chain( topics, episodes )
        else:
            return ()
