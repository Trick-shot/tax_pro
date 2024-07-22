from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path("",views.client_login, name='client_login'),
    path("register/", views.register_client, name='client_register'),
    path("logout/",views.client_logout ,name="client_logout"),
    path('home/products/', views.products, name='products'),
    path('home/stock', views.stock, name='stock')
    # 
]
