from django.urls import path

from .views import (
    TransactionListCreateAPIView,
    TransactionDetailAPIView,
    CategoryListAPIView,
    BalancedAPIView

)


urlpatterns = [

    path(
        "transactions/",
        TransactionListCreateAPIView.as_view()
    ),

    path(
        "transactions/<int:pk>/",
        TransactionDetailAPIView.as_view()
    ),
    path("categories/", CategoryListAPIView.as_view(), name="api-categories"),
    path("balance", BalancedAPIView.as_view(), name="api-balance"),
]