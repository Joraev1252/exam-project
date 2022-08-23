from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Account
from .models import ReportModel, InComeModel, ExpenseModel
from .forms import CreateReportForm, InComeForm, ExpenseForm


@login_required
def report_view(request):
    context = {}
    user = request.user
    admin_reports = ReportModel.objects.filter(author__is_admin=True)
    reports = ReportModel.objects.filter(author=user.id)
    all_reports = []
    for i in reports:
        all_reports.append(i)
    for j in admin_reports:
        all_reports.append(j)
    context['all_reports'] = all_reports
    return render(request, 'index.html', context)


@login_required
def add_report_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")
    form = CreateReportForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = ReportModel()
        if request.user.is_superuser:
            return redirect("report:vc_report")
        else:
            return redirect("report:report")
    context['form'] = form
    return render(request, "add.html", context)


@login_required
def report_detail_view(request, pk):
    context = {}
    report_detail = get_object_or_404(ReportModel, pk=pk)
    expense = ExpenseModel.objects.filter(report_expense_id=pk)
    income = InComeModel.objects.filter(report_id=pk)
    account = report_detail.author.email
    context['report_detail'] = report_detail
    context['expense'] = expense
    context['income'] = income
    context['account'] = account
    return render(request, 'report_detail.html', context)

@login_required
def add_income_view(request, pk):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")
    report = get_object_or_404(ReportModel, pk=pk)
    if request.user == report.author:
        form = InComeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.report = report
            obj.save()
            return redirect("report:report_detail", pk=pk)
    else:
        return HttpResponse("Sorry, you have any permission to add!")
    context['form'] = form
    return render(request, "income_add.html", context)


@login_required
def add_expense_view(request, pk):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("account:signin")
    report_expense = get_object_or_404(ReportModel, pk=pk)
    if request.user == report_expense.author:
        report_form = ExpenseForm(request.POST or None, request.FILES or None)
        if report_form.is_valid():
            obj = report_form.save(commit=False)
            obj.report_expense = report_expense
            obj.save()
            return redirect("report:report_detail", pk=pk)
    else:
        return HttpResponse("Sorry, you have any permission to add!")
    context['report_form'] = report_form
    return render(request, "expense_add.html", context)


@login_required
def vc_report_view(request):
    context = {}
    reports = ReportModel.objects.all()
    context['vc_all_reports'] = reports
    return render(request, 'vc_index.html', context)

