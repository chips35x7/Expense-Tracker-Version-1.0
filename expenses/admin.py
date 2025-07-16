from django.contrib import admin

from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'category',
        'amount',
        'date_created'
    ]


admin.site.register(Expense, ExpenseAdmin)