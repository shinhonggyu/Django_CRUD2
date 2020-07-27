from django.contrib import admin
from .models import Post

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at', 'updated_at']
    list_display_links = ['description']
