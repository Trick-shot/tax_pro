from django.contrib import admin
from .models import Client, Stock, Sales, Purchases, Profile

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'tin_number')

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('client', 'stock_type', 'quantity')
    list_filter = ('client', 'stock_type')

# @admin.register(Sales)
# class SalesAdmin(admin.ModelAdmin):
#     list_display = ('stock', 'date', 'quantity', 'unit_price', 'total_amount')
#     list_filter = ('stock', 'date')

# @admin.register(Purchases)
# class PurchasesAdmin(admin.ModelAdmin):
#     list_display = ('date', 'total_amount')

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('tin_number', 'stock_type', 'date', 'quantity')
