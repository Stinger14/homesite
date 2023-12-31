from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from functools import reduce
from operator import add

from expense_tracker.forms import ExpenseForm
from .models import Expense, Category, Budget

@login_required(login_url='login')
def add_expense(request):
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses')
        context = {'form': form}
        return render(request, 'expense_tracker/expenses.html', context)
    else:
        return render(request, 'expense_tracker/expense_form.html', {'form': form})

def update_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    context = {'form': form}
    return render(request, 'expense_tracker/expense_form.html', context)

def add_category(request):
    if request.method == 'POST':
        # Add the category
        pass
    else:
        # Display the form
        pass

def add_budget(request):
    if request.method == 'POST':
        # Add the budget
        pass
    else:
        # Display the form
        pass

def view_expenses(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expenses = reduce(add, [expense.amount for expense in expenses], 0)
    return render(request, 'expense_tracker/expenses.html', {'expenses': expenses, 'total_expenses': total_expenses})

def view_categories(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'expense_tracker/categories.html', {'categories': categories})

def view_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'expense_tracker/budgets.html', {'budgets': budgets})

def view_expenses_by_category(request, category_id):
    expenses = Expense.objects.filter(user=request.user, category=category_id)
    return render(request, 'expense_tracker/expenses.html', {'expenses': expenses})

