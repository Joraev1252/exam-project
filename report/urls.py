from django.urls import path
from report.views import *

app_name = 'report'

urlpatterns = [
    path('report/', report_view, name='report'),
    path('add_report/', add_report_view, name='add_report'),
    path('report_detail/<int:pk>', report_detail_view, name='report_detail'),
    path('add_income/<int:pk>', add_income_view, name='add_income'),
    path('add_expense/<int:pk>', add_expense_view, name='add_expense'),
    path('vc_report/', vc_report_view, name='vc_report'),
]

