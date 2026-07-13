from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Transaction
from apps.transactions.models import Transaction
from apps.transactions.api.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionListCreateAPIView(ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user,
            deleted_at__isnull=True
        )


class TransactionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        )

class TransactionListCreateAPIView(ListCreateAPIView):
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
    
class TransactionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        )