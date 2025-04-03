from django.db import models


class Account(models.Model):
    owner = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.owner} - Balance: {self.balance}"
