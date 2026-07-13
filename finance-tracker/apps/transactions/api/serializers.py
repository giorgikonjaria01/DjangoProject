from rest_framework import serializers
from apps.transactions.models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "category",
            "amount",
            "type",
            "description",
            "date",
        ]