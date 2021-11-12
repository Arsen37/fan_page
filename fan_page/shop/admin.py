from django.contrib import admin
from .models import *

class AttributesAdmin(admin.ModelAdmin):
    list_display = ['title','image','category','creation_date']
    list_display_links = ['title']
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Attributes,AttributesAdmin)

class AdminCategories(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,AdminCategories)

