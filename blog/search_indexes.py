#coding:utf-8
from haystack.indexes import SearchIndex,Indexable,CharField
from .models import Post

class PostIndex(SearchIndex, Indexable):
    text = CharField(document = True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

