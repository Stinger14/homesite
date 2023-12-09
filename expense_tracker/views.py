from django.shortcuts import render
from .models import Expense, Category, Budget

def add_expense(request):
    if request.method == 'POST':
        # Add the expense
        pass
    else:
        # Display the form
        pass

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
    return render(request, 'expense_tracker/expenses.html', {'expenses': expenses})

def view_categories(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, 'expense_tracker/categories.html', {'categories': categories})

def view_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'expense_tracker/budgets.html', {'budgets': budgets})

def view_expenses_by_category(request, category_id):
    expenses = Expense.objects.filter(user=request.user, category=category_id)
    return render(request, 'expense_tracker/expenses.html', {'expenses': expenses})

