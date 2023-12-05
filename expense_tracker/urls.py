from django.urls import path
from . import views

urlpatterns = [
    path('add_expense/', views.add_expense, name='add_expense'),
    path('expenses/', views.view_expenses, name='view_expenses'),
]
