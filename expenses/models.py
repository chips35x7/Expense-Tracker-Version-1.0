from django.db import models
from django.conf import settings

import uuid

expense_categories = {
    'Food': 'Food',
    'Transport': 'Transport',
    'Utilities': 'Utilities',
    'Housing': 'Housing',
    'Health': 'Health',
    'Entertainment': 'Entertainment',
    'Education': 'Education',
    'Shopping': 'Shopping',
    'Savings': 'Savings',
    'Debt': 'Debt',
    'Other': 'Other',
}

class Expense(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    category = models.CharField(max_length=30, choices=expense_categories)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.category