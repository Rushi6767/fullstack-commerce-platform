from .models import DemoModel
from django.db.models import Sum, Avg, Max, Min, Count


# ---------------------------
# BASIC QUERIES
# ---------------------------
def basic_queries():
    DemoModel.objects.all()
    DemoModel.objects.filter(status="active")
    DemoModel.objects.exclude(status="active")
    DemoModel.objects.get(id=1)


# ---------------------------
# LOOKUPS
# ---------------------------
def lookup_queries():
    DemoModel.objects.filter(integer_field__gt=10)
    DemoModel.objects.filter(integer_field__gte=10)
    DemoModel.objects.filter(integer_field__lt=10)
    DemoModel.objects.filter(integer_field__range=(10, 20))
    DemoModel.objects.filter(char_field__icontains="john")
    DemoModel.objects.filter(email_field__endswith="@gmail.com")
    DemoModel.objects.filter(id__in=[1, 2, 3])


# ---------------------------
# ORDERING + SLICING
# ---------------------------
def ordering_queries():
    DemoModel.objects.order_by("integer_field")
    DemoModel.objects.order_by("-integer_field")
    DemoModel.objects.all()[:5]
    DemoModel.objects.all()[5:10]


# ---------------------------
# AGGREGATION
# ---------------------------
def aggregation_queries():
    DemoModel.objects.aggregate(
        total=Sum("decimal_field"),
        avg=Avg("decimal_field"),
        max=Max("decimal_field"),
        min=Min("decimal_field"),
    )

    DemoModel.objects.values("status").annotate(
        count=Count("id")
    )


# ---------------------------
# UPDATE / DELETE
# ---------------------------
def update_delete_queries():
    DemoModel.objects.filter(id=3).update(status="inactive")
    DemoModel.objects.filter(integer_field__gt=30).update(status="blocked")

    DemoModel.objects.filter(id=5).delete()
    DemoModel.objects.all().delete()


# ---------------------------
# VALUES / PERFORMANCE
# ---------------------------
def value_queries():
    DemoModel.objects.values("char_field", "decimal_field")
    DemoModel.objects.values_list("char_field", "decimal_field")
    DemoModel.objects.values_list("char_field", flat=True)


# ---------------------------
# OPTIMIZATION
# ---------------------------
def optimization_queries():
    DemoModel.objects.only("char_field", "email_field")
    DemoModel.objects.defer("json_field", "text_field")

    DemoModel.objects.filter(status="active").exists()
    DemoModel.objects.count()