from django.shortcuts import render
from django.http import JsonResponse
from .models import DemoModel
from django.utils import timezone


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