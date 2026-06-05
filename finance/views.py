from django.shortcuts import render,redirect,get_object_or_404
from . models import Expense
# Create your views here.
def add_expense(request):
    expense=request.POST['title']
    amount=request.POST['amount']
    category=request.POST['category']
    Expense.objects.create(expense_name=expense,amount=amount,expense_category=category)
    return redirect('home')
def edit_expense(request,pk):
    get_expense=get_object_or_404(Expense,pk=pk)
    if request.method=='POST':
        new_expense=request.POST['expense_name']
        new_amount=request.POST['amount']
        new_category=request.POST['category']
        get_expense.expense_name=new_expense
        get_expense.amount=new_amount
        get_expense.expense_category=new_category
        get_expense.save()
        return redirect('home')
    else:
        context={
            'get_expense':get_expense,
        }
        return render(request,'edit_expense.html',context)

    

def delete_expense(request,pk):
    get_expense=get_object_or_404(Expense, pk=pk)
    get_expense.delete()
    return redirect('home')
    