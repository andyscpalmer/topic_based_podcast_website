from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeFormAdmin

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeFormAdmin
    model = CustomUser
    list_display = ['email', 'username', 'bio', 'twitter',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'bio',
            'twitter',
            'instagram',
            'website',
            'display_host',
            'pic_filename',
            'show_pic',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
