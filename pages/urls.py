from django.urls import path

from .views import (HomePageView,
                    AboutPageView,
                    PodhostList,
                    EpisodeListView,
                    EpisodePageView,
                    TopicListView,
                    TopicPageView,
                    UpdatePageView,
                    SearchResultsListView,)

from content.views import (EpisodeDetailView,
                        TopicDetailView,)

urlpatterns = [

    path('',
        HomePageView.as_view(),
        name='home'),

    path('aboutpage/',
        AboutPageView.as_view(),
        name='about'),

    path('episodes_page/',
        EpisodePageView.as_view(),
        name='episodes_page'),

    path('topics_page/',
        TopicPageView.as_view(),
        name='topics_page'),

    path('about/',
        PodhostList.as_view(),
        name='podhost_list'),

    path('episodes/',
        EpisodeListView.as_view(),
        name='episode_list'),

    path('episode/<slug:slug>/',
        EpisodeDetailView.as_view(),
        name='episode'),

    path('topics/',
        TopicListView.as_view(),
        name='topic_list'),

    path('topic/<slug:slug>/',
        TopicDetailView.as_view(),
        name='topic'),

    path('page/<int:pk>/update/',
        UpdatePageView.as_view(),
        name='update_page'),

    path('search/',
        SearchResultsListView.as_view(),
        name='search_results'),
]
