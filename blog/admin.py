from django.contrib import admin
from .models import Post, Author


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish")
    list_filter = ("author",)
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("user",)

