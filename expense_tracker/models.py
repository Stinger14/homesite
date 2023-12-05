from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Budget(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def total_expenses(self):
        return Expense.objects.filter(category=self.category, date__range=[self.start_date, self.end_date]).aggregate(Sum('amount'))['amount__sum'] or 0

    def remaining_budget(self):
        return self.amount - self.total_expenses()
