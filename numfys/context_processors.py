from django.conf import settings

# Make DOMAIN_NAME available in templates that are rendered with a RequestContext.
def get_domain_name(request):
    variable_dict = {
        'DOMAIN_NAME': settings.DOMAIN_NAME,
        }
    return variable_dict
