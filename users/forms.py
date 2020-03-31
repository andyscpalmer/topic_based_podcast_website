from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'bio', 'twitter',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'first_name',
            'last_name',
            'bio',
            'instagram',
            'twitter',
            'website',
            'display_host')

    def __init__(self, *args, **kwargs):
        """Remove finnicky 'password' field from user form"""
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        del self.fields['password']


class CustomUserChangeFormAdmin(UserChangeForm):
    """Keep 'password' field in user field for admin form"""

    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'bio',
            'instagram',
            'twitter',
            'website',
            'display_host')
