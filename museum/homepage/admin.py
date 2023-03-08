from django.contrib import admin

from .models import Post, Tag


admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'title',
        'text',
        'views',
        'created_on',
        'main_picture',
    )
    list_display_links = ('name',)
    filter_horizontal = ('tags',)
