from django import forms
from .models import Budget


class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = [
            "category",
            "amount",
            "month",
            "year"
        ]


    def clean_amount(self):

        amount = self.cleaned_data["amount"]

        if amount <= 0:
            raise forms.ValidationError(
                "Budget must be greater than zero"
            )

        return amount