from django import template
import markdown

register = template.Library()


@register.filter
def get_available(test_list):
    """Returns a list of tests that are available in the input list."""
    return test_list.filter(available=True)


@register.filter
def get_class(object):
    """Returns the class (Module, Example or Doc) of an object."""
    return object.__class__.__name__


@register.filter
def get_verbose(object):
    """Returns the verbose name of the class
    (Module, Example or Doc) of the object.
    """
    return object._meta.verbose_name


@register.filter
def markdownify(text):
    return markdown.markdown(text)
