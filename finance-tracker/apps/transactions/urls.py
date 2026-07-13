from django.urls import path
from .views import (
    TransactionListView,
    TransactionCreateView,
)
from .api_views import (
    TransactionListCreateAPIView,
    TransactionDetailAPIView
)


urlpatterns = [

    # Template views
    path(
        "",
        TransactionListView.as_view(),
        name="transaction-list"
    ),

    path(
        "create/",
        TransactionCreateView.as_view(),
        name="transaction-create"
    ),


    # DRF API
    path(
        "api/",
        TransactionListCreateAPIView.as_view(),
        name="transaction-api-list"
    ),

    path(
        "api/<int:pk>/",
        TransactionDetailAPIView.as_view(),
        name="transaction-api-detail"
    ),
    
]