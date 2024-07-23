from django.db import models
from django.conf import settings

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tin_number = models.IntegerField()

    def __str__(self):
        return f"Client: {self.user.email}"

class Stock(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    stock_type = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.stock_type}"

class Sales(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    unit_price = models.IntegerField(null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.stock_type}"

class Expenses(models.Model):
    Expenses = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.Expenses}"

class Purchases(models.Model):
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    total_amount = models.IntegerField(null=True, blank=True)

class Profile(models.Model):
    tin_number = models.IntegerField(null=True, blank=True)
    stock_type = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    quantity = models.CharField(max_length=15, null=True, blank=True)
