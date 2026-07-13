from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import TransactionForm
from django.db.models import Sum

class TransactionListView(LoginRequiredMixin, ListView):

    model = Transaction
    template_name = "transactions/list.html"
    context_object_name = "transactions"


    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user,
            deleted_at__isnull=True
        )



class TransactionCreateView(LoginRequiredMixin, CreateView):

    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/create.html"
    success_url = reverse_lazy("transaction-list")


    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)
    
class DashboardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard.html"


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        transactions = Transaction.objects.filter(
            user=self.request.user,
            deleted_at__isnull=True
        )

        income = transactions.filter(
            type="income"
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        expenses = transactions.filter(
            type="expense"
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        context["income"] = income
        context["expenses"] = expenses
        context["balance"] = income - expenses

        context["transactions"] = transactions[:5]


        return context