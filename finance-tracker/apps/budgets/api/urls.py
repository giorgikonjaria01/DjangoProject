from django.urls import path
from .views import BudgetListAPIView


urlpatterns = [
    path(
        "",
        BudgetListAPIView.as_view(),
        name="api-budgets"
    )
]