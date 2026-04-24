from django.views import View
from django.http import JsonResponse
from django.db.models import Sum, Avg, Max, Min, Count
from .models import DemoModel


class ORMPlaygroundView(View):

    def get(self, request):

        # ---------------- BASIC ----------------
        all_data = list(DemoModel.objects.all().values())
        active = list(DemoModel.objects.filter(status="active").values())

        # ---------------- LOOKUPS ----------------
        gt = list(DemoModel.objects.filter(integer_field__gt=10).values())
        range_q = list(DemoModel.objects.filter(integer_field__range=(10, 20)).values())

        # ---------------- ORDERING ----------------
        ordered = list(DemoModel.objects.order_by("-integer_field").values()[:5])

        # ---------------- AGGREGATION ----------------
        agg = DemoModel.objects.aggregate(
            total=Sum("decimal_field"),
            avg=Avg("decimal_field"),
            max=Max("decimal_field"),
            min=Min("decimal_field"),
        )

        # ---------------- GROUP BY ----------------
        grouped = list(
            DemoModel.objects.values("status").annotate(count=Count("id"))
        )

        # ---------------- EXISTS ----------------
        exists = DemoModel.objects.filter(status="active").exists()

        return JsonResponse({
            "all": all_data[:5],
            "active": active[:5],
            "gt": gt[:5],
            "range": range_q[:5],
            "ordered": ordered,
            "aggregation": agg,
            "grouped": grouped,
            "exists": exists,
        })