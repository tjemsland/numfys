from django.shortcuts import render
from django.db.models import Q

from notebook.models import Notebook
import re

# The following implementation of a search function is adapted from this
# blog post by Julien Phalip,
# http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """Split a query string into invidual keywords, getting rid of
    unecessary spaces and group quoted words together. Example:
    >>> normalize_query('some random  words "with   quotes " and spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
    """

    return [normspace(' ', (t[0] or t[1]).strip()) for t in
            findterms(query_string)]


def get_query(query_string, search_fields):
    """Return a query that is a combination of Q objects. That combination
    aims to search keywords within a model by testing the given search
    fields.
    """

    query = None  # Query to search for every search term
    terms = normalize_query(query_string)

    for term in terms:
        or_query = None  # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        search_fields = ['name', 'body', 'tags__name', 'topic__name', ]
        entry_query = get_query(query_string, search_fields)
        found_entries = \
            Notebook.objects.filter(entry_query, published=1).distinct().order_by('-pub_date')

    return render(request, template_name='search/search_results.html',
                  context={'query_string': query_string, 'notebooks':
                           found_entries}, )
