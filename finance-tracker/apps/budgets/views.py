from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Budget
from .forms import BudgetForm


class BudgetListView(LoginRequiredMixin, ListView):

    model = Budget
    template_name = "budgets/list.html"
    context_object_name = "budgets"


    def get_queryset(self):

        return Budget.objects.filter(
            user=self.request.user
        )



class BudgetCreateView(LoginRequiredMixin, CreateView):

    model = Budget
    form_class = BudgetForm
    template_name = "budgets/create.html"
    success_url = reverse_lazy("budget-list")


    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)