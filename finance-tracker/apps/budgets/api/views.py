from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import Budget
from .serializers import BudgetSerializer


class BudgetListAPIView(ListCreateAPIView):

    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(
            user=self.request.user
        )