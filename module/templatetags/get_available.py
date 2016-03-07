from django import template

register = template.Library()

# This template function is located in the module app dir because it has
# to be somewhere


@register.filter
def get_available(test_list):
    """Returns a list of tests that are available in the input list."""
    return test_list.filter(available=True)
