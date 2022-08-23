from django.contrib import admin
from .models import ReportModel, InComeModel, ExpenseModel

admin.site.register(ReportModel)
admin.site.register(InComeModel)
admin.site.register(ExpenseModel)