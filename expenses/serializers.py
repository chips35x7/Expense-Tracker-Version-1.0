from rest_framework import serializers

from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    """The serializer class for the Expense model"""
    class Meta:
        model = Expense
        fields = (
            'id',
            'category',
            'amount',
            'description',
            'created',
            'updated'
            )