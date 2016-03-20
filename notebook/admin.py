from django.contrib import admin
from django.forms.widgets import FileInput
from django.db import models
from notebook.models import Notebook, NotebookImage


class NotebookImageInline(admin.TabularInline):
    """Upload images in notebook admin page."""
    model = NotebookImage
    extra = 1
    # Remove 'Clear' checkbox in ordinary ImageField widget
    formfield_overrides = {models.ImageField: {'widget': FileInput}, }


class NotebookAdmin(admin.ModelAdmin):
    """Information on what to display and how in notebook admin page."""

    # Fill slug (url) automatically when filling in title
    prepopulated_fields = {'slug': ('title',)}

    # Attributes to list notebooks after. First attribute (title) becomes
    # the link to the specific notebook change page
    list_display = ['title', 'nb_type', 'edit_date', 'published', ]

    list_filter = ['nb_type', 'published', 'mo_topic', 'ex_topic',
                   'pub_date', 'edit_date', ]
    search_fields = ['title', 'published', 'nb_type', 'mo_topic',
                     'ex_topic', 'pub_date', 'edit_date', ]

    # Upload images in notebook admin page
    inlines = [NotebookImageInline, ]

    # Possible actions to ticked notebooks, apart from deletion
    actions = ['make_published', 'make_unpublished']

    # Custom make_published action message
    def make_published(self, request, queryset):
        rows_updated = queryset.update(published=1)
        if rows_updated == 1:
            message_bit = "1 notebook was"
        else:
            message_bit = "%s notebooks were" % rows_updated
        self.message_user(request, "%s successfully marked as published."
                          % message_bit)

    # Custom make_unpublished action message
    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(published=0)
        if rows_updated == 1:
            message_bit = "1 notebook was"
        else:
            message_bit = "%s notebooks were" % rows_updated
        self.message_user(request, "%s successfully marked as \
            unpublished." % message_bit)

    # Text in action dropdown
    make_published.short_description = "Mark selected notebooks as\
                                        published"
    make_unpublished.short_description = "Mark selected notebooks as \
                                          unpublished"

admin.site.register(Notebook, NotebookAdmin)
