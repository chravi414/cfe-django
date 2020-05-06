from django.contrib import admin
from posts.models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user',
                    'published_date', 'updated_at', 'created_at']
    search_fields = ['title', 'content']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
