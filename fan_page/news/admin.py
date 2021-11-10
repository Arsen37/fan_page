from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creation_date', 'image', 'slug')
    list_display_links = ('id',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class PostCategory(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, PostCategory)

class PostComents(admin.ModelAdmin):
    list_display = ('commentary','post')
    list_display_links = ('commentary',)

admin.site.register(Comentaries,PostComents)