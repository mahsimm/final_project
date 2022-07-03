from django_filters import rest_framework as filters
from accounts.models import Commodity, Category
from functools import reduce
from operator import or_
from django.db.models import Q


class ShoppingFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name="category__id", method='get_all')
    fromAmount = filters.NumberFilter(field_name='amount', lookup_expr='gt')
    toAmount = filters.NumberFilter(field_name='amount', lookup_expr='lt')

    def get_all(self, queryset, name, value):
        cats = Category.objects.filter(id=value)
        whilel = cats
        while True:
            extend_ = []
            query = reduce(or_, (Q(parent__id=cat.id)
                                 for cat in whilel))
            extend_ = Category.objects.filter(query)
            if len(extend_) == 0:
                break
            else:
                whilel = extend_
                cats = cats | whilel
        query = reduce(or_, (Q(category__id=cat.id) for cat in cats))
        return queryset.filter(query)

    class Meta:
        model = Commodity
        fields = ['category', 'fromAmount','toAmount']
