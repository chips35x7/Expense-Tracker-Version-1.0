from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['user', 'category', 'amount', 'created', 'updated']
    list_filter = ['category', 'created', 'updated']
    date_hierarchy = 'created'
    search_fields = ['category']
    ordering = ['-created']
    show_facets = admin.ShowFacets.ALWAYS
