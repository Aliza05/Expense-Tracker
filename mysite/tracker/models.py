from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    debit = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class Transaction(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    debit = models.IntegerField(default=0)
    credit = models.IntegerField(default=0)

    def __str__(self):
        return str(self.debit - self.credit)
