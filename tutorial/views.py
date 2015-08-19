from django.shortcuts import render
from datetime import date
from datetime import datetime
from elasticsearch import Elasticsearch

from haystack.generic_views import SearchView

class MySearchView(SearchView):
    """My custom search view."""

    # template = 'search.html'

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        # further filter queryset based on some set of criteria
        return queryset.filter(pub_date__gte=date(2015, 1, 1))

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        return context

    es = Elasticsearch()

    doc = {
        'handle': 'nickyollie',
        'text': 'this is confusing',
        'timestamp': datetime.now(),
    }

    res = es.index(index="test-index", doc_type="tweet", id=1, body=doc)
    print(res['created'])

    res = es.get(index="test_index", doc_type="tweet", id=1)
    print(res['source'])

    es.indices.refresh(index="test_index")

    res = es.search(index="test_index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s %(text)s" % hit["_source"])