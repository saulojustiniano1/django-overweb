from django.contrib import admin

from .models import *  # Post, Comment, Like

# from models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    # filter_horizontal = ("title", "content", "pub_date")
    search_fields = ("content",)
    list_filter = ("title",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post",)
    # filter_horizontal = ("title", "content", "pub_date")
    search_fields = ("content",)
    list_filter = ("post",)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("post",)
    # filter_horizontal = ("title", "content", "pub_date")
    search_fields = ("post",)
    list_filter = ("post",)


# admin.site.register(Comment)
# admin.site.register(Post)
