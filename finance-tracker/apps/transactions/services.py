from django.db.models import Sum
from .models import Transaction
from django.utils import timezone
import requests 
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




class CurrencyConverter(TransactionService):

    def convert(self, amount, from_currency, to_currency):

        response = requests.get(
            "https://api.exchangerate-api.com/v4/latest/GEL"
        )

        data = response.json()

        rate = data["rates"][to_currency]

        return amount * rate