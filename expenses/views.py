from rest_framework import generics

from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def perform_create(self, serializer):
        # return super().perform_create(serializer)
        serializer.save(user=self.request.user)