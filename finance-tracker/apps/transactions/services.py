from django.db.models import Sum
from .models import Transaction
from django.utils import timezone
import requests 
from django.conf import settings
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class TransactionService:

    def get_monthly_summary(self, user, month, year):

        transactions = Transaction.objects.filter(
            user=user,
            date__month=month,
            date__year=year,
            deleted_at__isnull=True
        )

        income = transactions.filter(
            type="income"
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        expenses = transactions.filter(
            type="expense"
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        return {
            "income": income,
            "expenses": expenses,
            "balance": income - expenses
        }



    def soft_delete(self, transaction):

        transaction.deleted_at = timezone.now()
        transaction.save()




class CurrencyConverter:

    def convert(
        self,
        amount,
        from_currency,
        to_currency
    ):

        rates = cache.get("exchange_rates")

        if not rates:

            response = requests.get(
                settings.EXCHANGE_API_URL
            )

            data = response.json()

            rates = data["rates"]

            cache.set(
                "exchange_rates",
                rates,
                3600
            )


        if from_currency == "GEL":
            return amount * rates[to_currency]

        return amount
    
