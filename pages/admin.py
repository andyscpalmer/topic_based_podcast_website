from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    """Allow admin to create and update pages"""
    list_display = ("title", "content",)

admin.site.register(Page, PageAdmin)
