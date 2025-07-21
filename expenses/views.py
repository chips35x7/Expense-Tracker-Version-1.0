from rest_framework import generics

from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsOwnerOrRestrictAccess

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Expense.objects.filter(user=self.request.user)
        return queryset

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrRestrictAccess,)
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()