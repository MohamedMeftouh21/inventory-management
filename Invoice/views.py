from django.contrib import admin
from dal import autocomplete
from .models import Product, Item


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Product.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
