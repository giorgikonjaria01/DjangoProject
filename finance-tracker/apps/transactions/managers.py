from django.db import models


class TransactionQuerySet(models.QuerySet):

    def active(self):
        return self.filter(
            deleted_at__isnull=True
        )


class TransactionManager(models.Manager):

    def get_queryset(self):

        return TransactionQuerySet(
            self.model,
            using=self._db
        )