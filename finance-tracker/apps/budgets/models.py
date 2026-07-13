from django.db import models
from django.conf import settings
from apps.transactions.models import Category


class Budget(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    month = models.IntegerField()

    year = models.IntegerField()


    def __str__(self):
        return f"{self.category.name} - {self.month}/{self.year}"