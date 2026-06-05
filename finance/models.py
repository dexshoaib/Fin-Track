from django.db import models

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES=[
        ('food', 'Food & Drinks'),
        ('bills', 'Bills & Utilities'),
        ('entertainment', 'Entertainment'),
        ('transport', 'Transport'),
        ('other', 'Other'),
    ]
    expense_name=models.CharField( max_length=250)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    expense_category=models.CharField(max_length=50 , choices=CATEGORY_CHOICES, default='other')
    created_at=models.DateTimeField( auto_now_add=True)
    modified_at=models.DateTimeField( auto_now=True)


    def __str__(self):
        return f"{self.expense_name} - {self.amount}"


