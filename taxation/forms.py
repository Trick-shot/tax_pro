from django import forms 
from django.core.exceptions import ValidationError

from core.models import User
from taxation.models import Client, Sales, Expenses


class ClientCreationForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    tin_number = forms.CharField(label='TIN NUMBER',
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TIN NUMBER'}))
    email = forms.EmailField(label='Email Address',
                                    widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password1 = forms.CharField(label='Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Retype Password',
                                     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype Password'}))
    
    class Meta:
        model = User
        fields = ['email','tin_number', 'full_name','password1', 'password2']


    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('loginPassword')
        password2 = cleaned_data.get('loginPassword2')
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
    def save(self, commit=True):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            full_name=self.cleaned_data['full_name'],
            password=self.cleaned_data['password1']
        )
        if commit:
            user.save()
            Client.objects.create(user=user,  tin_number=self.cleaned_data['tin_number'])
        return user


class ClientLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100,  widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='Password', max_length=100,  widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    
class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['stock', 'quantity', 'unit_price', 'total_amount']

class ExpensesForm(forms.ModelForm):
    
    
    class Meta:
        model = Expenses
        fields = ['Expenses', 'total_amount']