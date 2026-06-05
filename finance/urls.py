from django.urls import  path
from . import views
urlpatterns = [
   path('addexpense/',views.add_expense,name='addexpense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/',views.delete_expense,name='delete_expense'),

]