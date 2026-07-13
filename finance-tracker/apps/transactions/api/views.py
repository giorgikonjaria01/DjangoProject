from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from apps.transactions.models import Category, Transaction
from .serializers import TransactionSerializer, CategorySerializer
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from ..services import CurrencyConverter

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
    
class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Category.objects.filter(
            user=self.request.user
        )
    
class BalanceAPIView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):

        income = Transaction.objects.filter(
            user=request.user,
            type="income",
            deleted_at__isnull=True
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        expenses = Transaction.objects.filter(
            user=request.user,
            type="expense",
            deleted_at__isnull=True
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        return Response({
            "income": income,
            "expenses": expenses,
            "balance": income - expenses
        })
    
class ConvertCurrencyAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        amount = float(
            request.GET.get("amount")
        )

        to_currency = request.GET.get(
            "to"
        )

        converter = CurrencyConverter()

        result = converter.convert(
            amount,
            "GEL",
            to_currency
        )

        return Response({
            "converted": result
        })