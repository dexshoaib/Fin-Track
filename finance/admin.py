from django.contrib import admin
from . models import Expense
# Register your models here.
class Expenseadmin(admin.ModelAdmin):
    list_display=('expense_name','amount','expense_category','created_at','modified_at')
    search_fields=('expense_name',)

admin.site.register(Expense,Expenseadmin)
