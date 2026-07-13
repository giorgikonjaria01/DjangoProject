from rest_framework import serializers
from apps.transactions.models import Transaction, Category
from ..models import Category

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

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "type",
            "color"
        ]