from django.contrib import admin

from posts import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    # filter_horizontal = ("title",)
    search_fields = ("content",)
    list_filter = ("title",)
