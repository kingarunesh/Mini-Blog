from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "create_date", "last_updated"]
    list_display_links = ["id", "title", "create_date", "last_updated"]