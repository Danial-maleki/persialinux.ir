# Adminpanel/admin.py
from django.contrib import admin
from .models import News, Tutorial, Blog

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Blog, BlogAdmin)
