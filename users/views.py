from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import CustomUserChangeForm
from .models import CustomUser

class UpdateUser(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update host info"""
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('podhost_list')
    template_name = 'podhosts/update_podhost.html'
    login_url = 'login'

    def test_func(self):
        """Really make sure you're the correct host"""
        obj = self.get_object()
        return obj.username == self.request.user.username
