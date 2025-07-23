from django.db import models
from django.conf import settings

import uuid


class Expense(models.Model):
    """The model for user expenses"""
    class ExpenseCategories(models.TextChoices):
        FOOD = 'FD', 'Food'
        TRANSPORT = 'TRNSPT', 'Transport'
        UTILITIES = 'UTLTY', 'Utilities'
        HOUSING = 'HSING', 'Housing'
        HEALTH = 'HLTH', 'Health'
        ENTERTAINMENT = 'ENTTNMNT', 'Entertainment'
        EDUCATION = 'EDCTION', 'Education'
        SHOPPING = 'SHP', 'Shopping'
        SAVINGS = 'SVING', 'Savings'
        DEBT = 'DBT', 'Debt'
        OTHER = 'OTHR', 'Other'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    category = models.CharField(max_length=15, choices=ExpenseCategories)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Providing default sorting and indexing for faster queries on the 'created' database field"""
        ordering = ['-created']
        indexes = [
            models.Index(fields=['created'])
                ]
    
    def __str__(self):
        return self.category