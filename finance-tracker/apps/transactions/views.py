from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import TransactionForm


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
    
