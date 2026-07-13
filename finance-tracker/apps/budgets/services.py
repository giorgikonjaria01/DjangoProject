from django.db.models import Sum
from apps.transactions.models import Transaction


class BudgetService:


    def get_budget_warnings(self, user):

        warnings = []


        budgets = user.budget_set.all()


        for budget in budgets:

            spent = Transaction.objects.filter(
                user=user,
                category=budget.category,
                type="expense",
                date__month=budget.month,
                date__year=budget.year,
                deleted_at__isnull=True
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0


            if spent >= budget.amount * 0.8:

                warnings.append(
                    {
                        "category": budget.category.name,
                        "spent": spent,
                        "limit": budget.amount
                    }
                )


        return warnings