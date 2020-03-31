from django import forms
from .models import *
from django.forms.models import inlineformset_factory


class EpisodeForm(forms.ModelForm):
    """For episode information in create and update views"""

    class Meta:
        model = Episode
        exclude = ('slug', )


class TopicForm(forms.ModelForm):
    """For topic information in create and update views"""

    class Meta:
        model = Topic
        exclude = ('slug', )
