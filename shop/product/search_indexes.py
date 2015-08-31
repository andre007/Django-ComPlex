# coding=utf-8
from haystack import indexes
from product.models import Product


class ProductIndex(indexes.SearchIndex, indexes.Indexable):
    #text = indexes.CharField(document=True, use_template=True)
    #name = indexes.CharField(max_length=50, document=True)
    text = indexes.CharField(document=True, use_template=True)
    #full_text = indexes.CharField()
    #short_text = indexes.CharField()
    #price = indexes.IntegerField()

    def get_model(self):
        return Product

    #WTF???
    #def index_queryset(self, using=None):
    #    """Used when the entire index for model is updated."""
    #    return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())