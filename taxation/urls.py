from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path("",views.client_login, name='client_login'),
    path("register/", views.register_client, name='client_register'),
    path("logout/",views.client_logout ,name="client_logout"),
    path('home/sales/', views.sales, name='sales'),
    path('home/expenses/', views.expenses, name='expenses'),
    path('home/stock', views.stock, name='stock')
    # 
]
