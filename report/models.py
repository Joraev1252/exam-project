from django.db import models
from account.models import Account


class ReportModel(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    project = models.CharField(max_length=255)
    publish_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.project)

    @property
    def incomes(self):
        inc = []
        for i in self.income.all():
            inc.insert(0, int(i.month_income))
        if len(inc) > 1:
            this = inc[0]
            last = inc[1]
            x = this * 100 / last
            r = round(x)
            d = x - 100
            c = this - last
            if d > 0:
                return f"↑ {r}% ({c} so'm)"
            else:
                return f"↓ {r}% ({c} so'm)"
        else:
            return "ma'lumot yoq"

    @property
    def customers(self):
        customer = []
        for i in self.income.all():
            customer.insert(0, int(i.month_customer))
        if len(customer) > 1:
            this = customer[0]
            last = customer[1]
            x = this * 100 / last
            r = round(x)
            d = x - 100
            c = this - last
            if d > 0:
                return f"↑ {r}% ({c} ta ko'p)"
            else:
                return f"↓ {r}% ({c} ta ko'p)"
        else:
            return "ma'lumot yoq"

    @property
    def salary(self):
        salaryy = []
        for i in self.expense.all():
            salaryy.insert(0, int(i.salary))
        if len(salaryy) > 1:
            this = salaryy[0]
            last = salaryy[1]
            x = this * 100 / last
            r = round(x)
            d = x - 100
            c = this - last
            if d > 0:
                return f"↑ {r}% ({c} so'm ga ko'p)"
            else:
                return f"↓ {r}% ({c} so'm ga ko'p)"
        else:
            return "ma'lumot yoq"

    @property
    def advert(self):
        advertise = []
        for i in self.expense.all():
            advertise.insert(0, int(i.advertising))
        if len(advertise) > 1:
            this = advertise[0]
            last = advertise[1]
            x = this * 100 / last
            r = round(x)
            d = x - 100
            c = this - last
            if d > 0:
                return f"↑ {r}% ({c} ta ko'p)"
            else:
                return f"↓ {r}% ({c} ta ko'p)"
        else:
            return "ma'lumot yoq"


class InComeModel(models.Model):
    report = models.ForeignKey(ReportModel, related_name="income", on_delete=models.CASCADE)
    month_income = models.CharField(max_length=255)
    month_customer = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.report.project)


class ExpenseModel(models.Model):
    report_expense = models.ForeignKey(ReportModel, related_name="expense", on_delete=models.CASCADE)
    salary = models.CharField(max_length=255)
    advertising = models.CharField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.report_expense.project)
