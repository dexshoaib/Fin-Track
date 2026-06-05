from django.shortcuts import render
from django.db.models import Sum
from finance.models import Expense

def home(request):
    data = Expense.objects.aggregate(Sum('amount'))
    total = data['amount__sum'] or 0 
    expenses=Expense.objects.all()
    categories =Expense.objects.all()

    context={
        'total_spent':total,
        'expenses':expenses,
        
    }

    return render(request,'home.html',context)