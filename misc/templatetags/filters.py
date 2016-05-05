from django import template
import markdown

register = template.Library()


@register.filter
def get_nbtype(notebook):
    """Return the notebook type, i.e. module or example."""
    return notebook.topic.nb_type


@register.filter
def markdownify(text):
    """Render Markdown text. Use e.g. in the flatpages app."""
    return markdown.markdown(text)
