from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls), # Change the admin url so nefarious hackers don't come snooping

    # User management
    path('hidden_user_authentication/', include('allauth.urls')), # Do the same thing for user logins

    # Local apps
    path('', include('pages.urls')),
    path('users/', include('users.urls')),
    path('content/', include('content.urls')),
]
