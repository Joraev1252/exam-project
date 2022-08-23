from django import forms
from .models import ReportModel, InComeModel, ExpenseModel


class CreateReportForm(forms.ModelForm):
    class Meta:
        model = ReportModel
        fields = ['project']


class InComeForm(forms.ModelForm):
    class Meta:
        model = InComeModel
        fields = ['month_income', 'month_customer']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenseModel
        fields = ['salary', 'advertising']

