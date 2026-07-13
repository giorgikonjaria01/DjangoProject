from datetime import date, timedelta
import calendar

from apps.transactions.models import Transaction

STUDENT_ID = 7360
VARIANT = STUDENT_ID % 3


def next_month_date(current_date):
    year = current_date.year
    month = current_date.month + 1

    if month > 12:
        month = 1
        year += 1

    day = current_date.day
    last_day = calendar.monthrange(year, month)[1]

    # Normal case
    if day <= last_day:
        return date(year, month, day)

    # Edge case: requested day doesn't exist

    if VARIANT == 0:
        # Last business day
        d = date(year, month, last_day)

        while d.weekday() >= 5:
            d -= timedelta(days=1)

        return d

    elif VARIANT == 1:
        # First day of the month
        return date(year, month, 1)

    elif VARIANT == 2:
        # Skip this occurrence
        return None


def generate_recurring_transactions():
    today = date.today()

    recurring_transactions = Transaction.objects.filter(
        recurrence_rule__in=["daily", "weekly", "monthly"],
        next_occurrence__lte=today,
        deleted_at__isnull=True,
    )

    for transaction in recurring_transactions:

        Transaction.objects.create(
            user=transaction.user,
            category=transaction.category,
            amount=transaction.amount,
            description=transaction.description,
            type=transaction.type,
            recurrence_rule=transaction.recurrence_rule,
            next_occurrence=transaction.next_occurrence,
        )

        if transaction.recurrence_rule == "daily":
            transaction.next_occurrence += timedelta(days=1)

        elif transaction.recurrence_rule == "weekly":
            transaction.next_occurrence += timedelta(days=7)

        elif transaction.recurrence_rule == "monthly":
            new_date = next_month_date(transaction.next_occurrence)

            if new_date is None:
                # Variant 2: skip this month
                next_month = transaction.next_occurrence.replace(day=1)
                if next_month.month == 12:
                    next_month = next_month.replace(
                        year=next_month.year + 1,
                        month=1,
                    )
                else:
                    next_month = next_month.replace(
                        month=next_month.month + 1,
                    )

                transaction.next_occurrence = next_month_date(next_month)

            else:
                transaction.next_occurrence = new_date

        transaction.save()