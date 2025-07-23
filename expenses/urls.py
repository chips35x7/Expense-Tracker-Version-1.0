from rest_framework import routers
from .views import ExpenseViewSet

# Generating URLs for the list and detail endpoints
router = routers.SimpleRouter()
router.register('', ExpenseViewSet, basename='expenses')

urlpatterns = router.urls