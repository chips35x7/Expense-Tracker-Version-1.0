from rest_framework import viewsets

from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsOwnerOrRestrictAccess


class ExpenseViewSet(viewsets.ModelViewSet):
    """Viewset for listing user expenses and viewing expense details"""
    serializer_class = ExpenseSerializer
    permission_classes = (IsOwnerOrRestrictAccess,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        return queryset