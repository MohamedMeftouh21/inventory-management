from django.urls import path
from .views import ProductAutocomplete

urlpatterns = [
    path('product-autocomplete/', ProductAutocomplete.as_view(), name='product-autocomplete'),
    # Add other URLs for your views if needed
]
