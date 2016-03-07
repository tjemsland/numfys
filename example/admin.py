from django.contrib import admin
from django.forms.widgets import FileInput
from django.db import models

from example.models import Example, ExampleImage


class ExampleImageInline(admin.TabularInline):
    model = ExampleImage
    extra = 1
    # Remove 'Clear' checkbox in ordinary ImageField widget
    formfield_overrides = {models.ImageField: {'widget': FileInput}, }


class ExampleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'topic', 'pub_date', 'edit_date', ]
    list_filter = ['topic', 'pub_date', 'edit_date', ]
    search_fields = ['title', 'topic', 'pub_date', 'edit_date', ]
    inlines = [ExampleImageInline, ]

admin.site.register(Example, ExampleAdmin)
