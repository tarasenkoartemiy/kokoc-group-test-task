from django.contrib import admin
from .models import Сurrency, Rate

admin.site.site_header = "Kokoc Group"
admin.site.index_title = "Это простая админ панель ;)"


@admin.register(Сurrency)
class СurrencyAdmin(admin.ModelAdmin):
    list_display = ["char_code", "name"]
    search_fields = ["char_code__istartswith"]


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ["date", "value", "currency"]
    list_filter = ["currency__char_code"]
    search_fields = ["date__istartswith"]
