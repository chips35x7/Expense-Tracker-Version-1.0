from django.urls import path

from .views import *

urlpatterns = [
    path('', ExpenseList.as_view())
]