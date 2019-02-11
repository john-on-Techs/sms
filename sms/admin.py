from django.contrib import admin
from .models import SaleRecord, Product, Station, StationProductPrice, UserStation


# Register your models here.


class SaleRecordAdmin(admin.ModelAdmin):
    # fields =['pub_date','question_text']
    # fieldsets = [
    #     ('User', {'fields': ['user']}),
    #     ('Product', {'fields': ['product']}),
    #     ('Number of Litres', {'fields': ['number_of_litres']}),
    #     ('Station', {'fields': ['station']}),
    #
    # ]

    list_display = ('station', 'product', 'number_of_litres', 'price_per_litre', 'amount_collected', 'entry_at')
    list_filter = ['entry_at']
    search_fields = ['station__name']


admin.site.register(SaleRecord, SaleRecordAdmin)
admin.site.register(Product)
admin.site.register(UserStation)
admin.site.register(StationProductPrice)
admin.site.register(Station)

