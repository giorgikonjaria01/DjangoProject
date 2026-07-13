from django.db import models
from apps.accounts.models import User
from .managers import TransactionManager

class Category(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="categories"
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Transaction(models.Model):

    INCOME = "income"
    EXPENSE = "expense"

    TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    description = models.TextField(
        blank=True
    )

    date = models.DateField()

    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )
    
    objects = TransactionManager()

    RECURRENCE_CHOICES = [
    ("none", "None"),
    ("daily", "Daily"),
    ("weekly", "Weekly"),
    ("monthly", "Monthly"),
]

    recurrence_rule = models.CharField(
        max_length=10,
        choices=RECURRENCE_CHOICES,
        default="none",
    )

    next_occurrence = models.DateField(
        null=True,
        blank=True,
    )


    def __str__(self):
        return f"{self.type}: {self.amount}"