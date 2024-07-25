from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import admin

from core.models import User
from .models import Client, Sales, Purchases, Stock, Expenses
from .forms import ClientCreationForm, ClientLoginForm, ExpensesForm, SalesForm


def register_client(request): 
    template_name = 'client/register.html'
    
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_login')
    else:
        form = ClientCreationForm()
        
    return render(request, template_name, {'form': form})    


def client_login(request):
    template_name = 'client/login.html'
    
    if request.method == 'POST':
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            client = authenticate(request, email=email, password=password)
            if client:
                login(request, client)
                return redirect('home')
            else:
                form.add_error(None, "Invalid email address or password.")
    else:
        form = ClientLoginForm()
        
    return render(request, template_name, {'form': form})


def client_logout(request):
    logout(request)
    return redirect('client_login')


@login_required
def index(request):
    template_name = 'client/index.html'
    if request.user.is_authenticated and hasattr(request.user, 'client'):
    
        sales = Sales.objects.all()

        total_sales = Sales.objects.aggregate(total_sales=Sum('total_amount'))['total_sales']
        total_sales_amount = total_sales if total_sales else 0

        total_purchases = Expenses.objects.aggregate(total_purchase=Sum('total_amount'))['total_purchase']
        total_purchase_amount = total_purchases if total_purchases else 0

        net_profit = total_sales_amount - total_purchase_amount

        tax_to_be_paid = 0
        if total_sales_amount <= 3000000:
            tax_to_be_paid = 0
        elif total_sales_amount > 3000000 and total_sales_amount <= 10000000:
            tax_to_be_paid = total_sales_amount * 0.03
        elif total_sales_amount > 10000000 and total_sales_amount <= 100000000:
            tax_to_be_paid = total_sales_amount * 0.045
        elif total_sales_amount > 100000000:
            tax_to_be_paid = total_sales_amount * 0.06

     
    else:
        sales = 0

        total_sales = 0
        total_sales_amount = 0

        total_purchases = 0
        total_purchase_amount = 0
    
    data = {
            "total_sales_amount": total_sales_amount,
            "total_purchase_amount": total_purchase_amount,
            "net_profit": net_profit,
            "tax_to_be_paid": tax_to_be_paid,
            "sales": sales,
        }
        

    return render(request, template_name, context=data)


@login_required
def sales(request):
    template_name = 'client/sales.html'
    if request.user.is_authenticated and hasattr(request.user, 'client'):
       sales = Sales.objects.all()
    else:
        sales = Sales.objects.none()
    
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales')
    else:
        form = SalesForm()
        
    return render(request, template_name, {"sales": sales, "form": form})


@login_required
def expenses(request):
    template_name = 'client/expenses.html'
    if request.user.is_authenticated and hasattr(request.user, 'client'):
       expenses = Expenses.objects.all()
    else:
        expenses = Expenses.objects.none()
         
    
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    else:
        form = ExpensesForm()
        
    return render(request, template_name, {"expenses": expenses, "form": form})


@login_required
def stock(request):
    if request.user.is_authenticated and hasattr(request.user, 'client'):
        client = request.user.client
        stocks = Stock.objects.filter(client=client)
    else:
        stocks = Stock.objects.none()
    
    return render(request, 'client/stock.html', {'stocks': stocks})
