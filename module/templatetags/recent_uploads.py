from module.models import Module
from itertools import chain
from django import template

register = template.Library()


# This template function is located in the module app dir because it has
# to be somewhere
@register.assignment_tag
def recent_uploads():
    """Returns the last four published objects
    (module, example or document) as a list.
    """
    # Sorts every module, example and doc by date to one list, saves the last
    # three to another list and reverses the order
    objects = sorted(
        chain(Module.objects.all()),
        key=lambda object: object.pub_date)
    recent_objects = objects[-4:]
    recent_objects.reverse()

    # If object is module or example, strip of first four characters
    for object in recent_objects:
        if (object.__class__.__name__ == 'Module'):
            object.title = object.title[4:]
        else:
            pass

    return recent_objects


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
