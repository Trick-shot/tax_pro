from django.db import models
from django.conf import settings
from django.db.models import Sum

class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tin_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Client: {self.user.email}"
    
    def get_full_name(self):
        return f"{self.user.full_name}"

    get_full_name.short_description = 'Full Name'
    
    def get_total_sales_amount(self):
        total_sales = Sales.objects.filter(stock__client=self).aggregate(total_sales=Sum('total_amount'))['total_sales']
        return total_sales if total_sales else 0

    def get_tax_to_be_paid(self):
        total_sales_amount = self.get_total_sales_amount()
        if total_sales_amount <= 3000000:
            return 0
        elif total_sales_amount <= 10000000:
            return total_sales_amount * 0.03
        elif total_sales_amount <= 100000000:
            return total_sales_amount * 0.045
        else:
            return total_sales_amount * 0.06
    
    get_tax_to_be_paid.short_description = 'Tax to be Paid'

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

    def save(self, *args, **kwargs):
        if self.pk is None:  
            self.total_amount = self.quantity * self.unit_price
            super().save(*args, **kwargs)
            self.stock.quantity -= self.quantity
            self.stock.save()
        else:
            super().save(*args, **kwargs)
            
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
