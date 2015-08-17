from django.shortcuts import render
from datetime import date

from haystack.generic_views import SearchView

class MySearchView(SearchView):
    """My custom search view."""

    template = 'search.html'

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        # further filter queryset based on some set of criteria
        return queryset.filter(pub_date__gte=date(2015, 1, 1))

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        return context