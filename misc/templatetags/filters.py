from django import template
import markdown
register = template.Library()


@register.filter
def get_modules(notebook_list):
    """Return notebooks in list which are modules and published."""
    return notebook_list.filter(nb_type='M', published=1)


@register.filter
def get_examples(notebook_list):
    """Return notebooks in list which are examples and published."""
    return notebook_list.filter(nb_type='E', published=1)


@register.filter
def get_nbtype(notebook):
    """Return the notebook type, i.e. module or example."""
    return notebook.nb_type


@register.filter
def markdownify(text):
    """Render Markdown text. Use e.g. in the flatpages app."""
    return markdown.markdown(text)
