from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal


class OperationType(models.TextChoices):
    IN = "IN"
    OUT = "OUT"


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    operation_type = models.CharField(
        max_length=3,
        choices=OperationType,
        default=OperationType.OUT,
    )
    value = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal(0))]
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    link_nf = models.URLField(null=True, blank=True)
    date_time = models.DateTimeField(default=timezone.now)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.pk}"


class Pending(models.Model):
    operation_type = models.CharField(
        max_length=3,
        choices=OperationType,
        default=OperationType.OUT,
    )
    value = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(Decimal(0))]
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    link_nf = models.URLField(null=True, blank=True)
    date_time = models.DateTimeField(default=timezone.now)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT, null=True, blank=True)
    payed = models.BooleanField()
    movement = models.ForeignKey(
        Transaction, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return f"{self.pk}"
