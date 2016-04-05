from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html


# Define a new FlatPageAdmin
class ExtendedFlatPageAdmin(FlatPageAdmin):
    readonly_fields = ('flatpage_info',)

    def flatpage_info(self, instance):
        return format_html('{} <a href="https://pypi.python.org/pypi/Markdown">{}</a>.<br>{} <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet">{}</a>.',
                           'You can write both Markdown and HTML code in the \
            content field. We use the',
                           'Python implementation of Markdown',
                           'For how to write Markdown text, check out this',
                           'Markdown Cheatsheet on GitHub'
                           )

    fieldsets = (
        (None, {'fields': ('flatpage_info', 'url', 'title', 'content',
                           'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse', ),
            'fields': (
                'registration_required',
                'template_name',
            ),
        }),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ExtendedFlatPageAdmin)
