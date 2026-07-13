from django.urls import path

from .views import (
    TransactionListCreateAPIView,
    TransactionDetailAPIView
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

]