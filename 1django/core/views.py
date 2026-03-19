from django.shortcuts import render
from django.http import JsonResponse
from .models import DemoModel
from django.utils import timezone
from django.db.models import Avg, Max, Min, Sum, Count


# Create your views here.

def create_one(request):
    obj = DemoModel.objects.create(
        char_field="First Record",
        text_field="Hello world",
        integer_field=10,
        positive_integer_field=5,
        float_field=2.5,
        decimal_field=10.50,
        boolean_field=True,
        date_field=timezone.now().date(),
        datetime_field=timezone.now(),
        time_field=timezone.now().time(),
        status="active",
        url_field="https://example.com",
        email_field="test@example.com",
        json_field={"key": "value"},
    )

    return JsonResponse({
        "message": "One record created",
        "id": obj.id
    })


def create_many(request):
    ids = []

    for i in range(5):
        obj = DemoModel.objects.create(
            char_field=f"Record {i}",
            text_field="Bulk insert test",
            integer_field=i,
            positive_integer_field=i + 1,
            float_field=float(i) + 0.5,
            decimal_field=10.0 + i,
            boolean_field=(i % 2 == 0),
            date_field=timezone.now().date(),
            datetime_field=timezone.now(),
            time_field=timezone.now().time(),
            status="active",
            url_field="https://example.com",
            email_field=f"user{i}@example.com",
            json_field={"index": i},
        )
        ids.append(obj.id)

    return JsonResponse({
        "message": "5 records created",
        "ids": ids
    })

def get_all(request):
    data = list(DemoModel.objects.values())

    return JsonResponse({
        "count": len(data),
        "data": data
    })


def get_one(request, id):
    try:
        obj = DemoModel.objects.get(id=id)

        return JsonResponse({
            "id": obj.id,
            "char_field": obj.char_field,
            "text_field": obj.text_field,
            "integer_field": obj.integer_field,
            "positive_integer_field": obj.positive_integer_field,
            "float_field": obj.float_field,
            "decimal_field": str(obj.decimal_field),
            "boolean_field": obj.boolean_field,
            "status": obj.status,
            "json_field": obj.json_field,
        })

    except DemoModel.DoesNotExist:
        return JsonResponse({
            "error": "Record not found"
        }, status=404)
    

def update_one(request, id):
    try:
        obj = DemoModel.objects.get(id=id)

        obj.char_field = "Updated Record"
        obj.integer_field = 999
        obj.boolean_field = False
        obj.json_field = {"updated": True}
        obj.datetime_field = timezone.now()

        obj.save()

        return JsonResponse({
            "message": "Record updated",
            "id": obj.id
        })

    except DemoModel.DoesNotExist:
        return JsonResponse({
            "error": "Record not found"
        }, status=404)
    
def delete_one(request, id):
    try:
        obj = DemoModel.objects.get(id=id)
        obj.delete()

        return JsonResponse({
            "message": "Record deleted",
            "id": id
        })

    except DemoModel.DoesNotExist:
        return JsonResponse({
            "error": "Record not found"
        }, status=404)
    

"""
SELECT * FROM demo_model;

SELECT * FROM demo_model
WHERE id = 3;

SELECT *
FROM demo_model
WHERE status='active';

SELECT *
FROM demo_model
WHERE status != 'active';

SELECT *
FROM demo_model
ORDER BY id
LIMIT 1;

SELECT *
FROM demo_model
ORDER BY id DESC
LIMIT 1;


Step 2: Filter Data
SELECT * FROM core_demomodel
WHERE status = 'active';

SELECT *
FROM core_demomodel
WHERE decimal_field > 90000;

SELECT *
FROM core_demomodel
WHERE integer_field >= 30;

SELECT *
FROM core_demomodel
WHERE char_field LIKE '%John%';

SELECT *
FROM core_demomodel
WHERE id IN (1,3,5,7);

SELECT *
FROM core_demomodel
WHERE integer_field BETWEEN 25 AND 30;

-- ORDER BY ASC
SELECT *
FROM core_demomodel
ORDER BY integer_field;

-- ORDER BY DESC
SELECT *
FROM core_demomodel
ORDER BY integer_field DESC;

-- ORDER BY Name
SELECT *
FROM core_demomodel
ORDER BY char_field;

-- Multiple ORDER BY
SELECT *
FROM core_demomodel
ORDER BY status, integer_field DESC;

-- LIMIT 5
SELECT *
FROM core_demomodel
LIMIT 5;

-- OFFSET 5 LIMIT 5
SELECT *
FROM core_demomodel
LIMIT 5 OFFSET 5;

SELECT COUNT(*) FROM core_demomodel;

SELECT EXISTS(
SELECT *
FROM core_demomodel
WHERE status='active'
);

SELECT
SUM(decimal_field),
AVG(decimal_field),
MAX(decimal_field),
MIN(decimal_field)
FROM core_demomodel;

SELECT
status,
COUNT(*)
FROM core_demomodel
GROUP BY status;
otuput:
[
    {
        "status":"active",
        "total":7
    },
    {
        "status":"inactive",
        "total":2
    },
    {
        "status":"blocked",
        "total":1
    }
]

UPDATE core_demomodel
SET status='inactive'
WHERE id=3;

UPDATE core_demomodel
SET status='blocked'
WHERE integer_field > 30;

DELETE
FROM core_demomodel
WHERE id = 1;

DELETE
FROM core_demomodel
WHERE status='inactive';

DELETE FROM core_demomodel;

SELECT
char_field,
decimal_field
FROM core_demomodel;
"""

def orm(request):
    # SELECT * FROM demo_model;
    # data = list(DemoModel.objects.all().values())
    # print("DATA : =============================================", data)

    # obj = DemoModel.objects.get(id=10)

    # filter_data = list(
    #     DemoModel.objects.filter(
    #         status="active"
    #     ).values()
    # )

    # exclude_data = list(
    #     DemoModel.objects.exclude(
    #         status="active"
    #     ).values()
    # )

    # first_data = DemoModel.objects.first()

    # last_data = DemoModel.objects.last()

    # filter data
    # exact_data = list(
    #     DemoModel.objects.exclude(
    #         status="active"
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         decimal_field__gt=90000
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         integer_field__gte=30
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         integer_field__lt=30
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         integer_field__lte=28
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         char_field__contains="John"
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         char_field__icontains="john"
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         char_field__startswith="J"
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         email_field__endswith="@example.com"
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         id__in=[1, 3, 5, 7]
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         integer_field__range=(25, 30)
    #     ).values()
    # )

    # data = list(
    #     DemoModel.objects.filter(
    #         file_field__isnull=True
    #     ).values()
    # )

    # data = list(DemoModel.objects.filter(status = 'inactive').values())
    # print("DAta ===================================", data)

    # ORDER BY ASC
    data = list(
        DemoModel.objects.order_by("integer_field").values()
    )

    # ORDER BY DESC
    data = list(
        DemoModel.objects.order_by("-integer_field").values()
    )

    # ORDER BY Name
    data = list(
        DemoModel.objects.order_by("char_field").values()
    )

    # Multiple ORDER BY
    data = list(
        DemoModel.objects.order_by("status", "-integer_field").values()
    )

    # Reverse
    data = list(
        DemoModel.objects.order_by("integer_field").reverse().values()
    )

    # LIMIT 5
    data = list(
        DemoModel.objects.all()[:5].values()
    )

    # OFFSET 5 LIMIT 5
    data = list(
        DemoModel.objects.all()[5:10].values()
    )

    data = DemoModel.objects.aggregate(

    total_salary=Sum("decimal_field"),

    average_salary=Avg("decimal_field"),

    highest_salary=Max("decimal_field"),

    lowest_salary=Min("decimal_field")

    )

    count = DemoModel.objects.count()
    exists = DemoModel.objects.filter(
    status="active"
    ).exists()

    data = DemoModel.objects.aggregate(
    total=Sum("decimal_field")
    )

    data = DemoModel.objects.aggregate(
    average=Avg("decimal_field")
    )

    data = DemoModel.objects.aggregate(
    maximum=Max("decimal_field")
    )
    data = DemoModel.objects.aggregate(
    maximum=Min("decimal_field")
    )

    data = list(
    DemoModel.objects.values("status")
    .annotate(total=Count("id"))
    )

    obj = DemoModel.objects.get(id=1)
    obj.char_field = "Rushi"
    obj.integer_field = 100
    obj.save()

    rows = DemoModel.objects.filter(
    id=3
    ).update(
        status="inactive"
    )

    rows = DemoModel.objects.filter(
    integer_field__gt=30
    ).update(
        status="blocked"
    )

    # obj = DemoModel.objects.get(id=1)
    # obj.delete()

    # deleted_count, _ = DemoModel.objects.filter(
    # status="inactive"
    # ).delete()

    # deleted_count, _ = DemoModel.objects.all().delete()

    # if DemoModel.objects.filter(id=5).exists():
    #     DemoModel.objects.filter(id=5).delete()


    data = list(
    DemoModel.objects.values(
        "char_field",
        "decimal_field"
    )
    )
    data = list(
    DemoModel.objects.values_list(
        "char_field",
        "decimal_field"
    )
    )

    data = list(
    DemoModel.objects.values_list(
        "char_field",
        flat=True
    )
    )

    users = DemoModel.objects.only(
    "char_field",
    "email_field"
    )

    for user in users:
        print(user.char_field)
        print(user.email_field)

    users = DemoModel.objects.defer(
    "json_field",
    "text_field"
)

    for user in users:
        print(user.char_field)




    return JsonResponse({
        # "count": len(data),
        # "data": data

        # "id": obj.id,
        # "name": obj.char_field,
        # "salary": float(obj.decimal_field)

        # "count": len(data),
        # "data": filter_data

        # "count": len(data),
        # "data": exclude_data

        # "data": first_data

        # "data": last_data

        # "data": last_data

        "data" : data
    })