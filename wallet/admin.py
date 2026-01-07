from django.contrib import admin
from .models import Category, Transaction, Wallet, Pending


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "value",
        "operation_type",
        "wallet",
        "category",
        "date_time",
        "description",
    ]
    list_filter = ["operation_type", "date_time", "wallet", "category"]


@admin.register(Pending)
class PendingAdmin(admin.ModelAdmin):
    list_display = [
        "value",
        "operation_type",
        "wallet",
        "category",
        "date_time",
        "description",
        "payed",
    ]
    list_filter = ["operation_type", "payed", "date_time", "wallet", "category"]
