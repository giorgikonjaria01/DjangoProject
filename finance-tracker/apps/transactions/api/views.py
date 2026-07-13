from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.transactions.models import Transaction
from .serializers import TransactionSerializer


class TransactionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user,
            deleted_at__isnull=True
        )


    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class TransactionDetailAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        )