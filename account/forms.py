from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from account.models import Account


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")

    class Meta:
        model = Account
        fields = ['email', 'full_name', 'password1', 'password2']


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid inputs")


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'full_name'
        ]
        enctype = "multipart/form-data"

