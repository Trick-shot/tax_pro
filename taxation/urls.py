from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path("login/",views.client_login, name='client_login'),
    path("register/", views.register_client, name='client_register'),
    path("logout/",views.client_logout ,name="client_logout")
]
