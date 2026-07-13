from django.urls import path

from .views import (
    ConvertCurrencyAPIView,
    TransactionListCreateAPIView,
    TransactionDetailAPIView,
    CategoryListAPIView,
    BalanceAPIView

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
    path("balance", BalanceAPIView.as_view(), name="api-balance"),
    path("convert/", ConvertCurrencyAPIView.as_view(), name="api-convert")
]