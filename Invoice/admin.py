from django.contrib import admin
from django.contrib import messages
from .models import Product, Item, Invoice
from django.forms import TextInput
from django.db.models import Q
from dal import autocomplete





@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
@admin.register(Item)

class ItemAdmin(admin.ModelAdmin):
    form = autocomplete.FutureModelForm
    autocomplete_fields = ['product']





class ItemInline(admin.TabularInline):
    model = Invoice.items.through
    


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ('id', 'date', 'total_amount')
    exclude = ('items',)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            product = instance.item.product
            quantity = instance.item.quantity
            if product.quantity >= quantity:
                product.quantity -= quantity
                product.save()
                instance.save()
            else:
                messages.error(request, f"Insufficient quantity for product: {product.name}")
        formset.save_m2m()

        self.save_model(request, form.instance, form, change)

    def save_model(self, request, obj, form, change):
        obj.save() 

        # Calculate total amount using the associated items
        obj.total_amount = sum(item.quantity * item.product.price for item in obj.items.all())
        obj.save()


admin.site.register(Invoice, InvoiceAdmin)


