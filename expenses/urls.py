from django.urls import path

from .views import *

urlpatterns = [
    path('', ExpenseList.as_view()),
    path('<uuid:pk>', ExpenseDetail.as_view()),
]