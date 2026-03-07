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

    last_data = DemoModel.objects.last()



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

        "data": last_data        
    })