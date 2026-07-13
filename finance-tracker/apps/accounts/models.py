from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    currency = models.CharField(
        max_length=3,
        default="GEL"
    )

    def __str__(self):
        return self.username