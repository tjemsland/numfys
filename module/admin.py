from django.contrib import admin
from django.forms.widgets import FileInput
from django.db import models

from module.models import Module, ModuleImage


class ModuleImageInline(admin.TabularInline):
    model = ModuleImage
    extra = 1
    # Remove 'Clear' checkbox in ordinary ImageField widget
    formfield_overrides = {models.ImageField: {'widget': FileInput}, }


class ModuleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'topic', 'pub_date', 'edit_date', ]
    list_filter = ['topic', 'pub_date', 'edit_date', ]
    search_fields = ['title', 'topic', 'pub_date', 'edit_date', ]
    inlines = [ModuleImageInline, ]

admin.site.register(Module, ModuleAdmin)
