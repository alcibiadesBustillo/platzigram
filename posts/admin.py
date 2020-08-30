#Django
from django.contrib import admin

from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Profile Admin"""
    list_display = ('pk', 'user', 'title', 'photo')
    list_display_links = ('pk', 'user',)
    list_editable = ('title', 'photo')

    search_fields = (
        'title',                
    )

    list_filter = (        
        'created',
        'modified',        
    )

    fieldsets = (
        ('Post', {
            'fields': (('title', 'photo'),),
        }),        
        ('Metadata', {
            'fields': (('created', 'modified'),),
        }),
    )
    readonly_fields = ('created', 'modified')