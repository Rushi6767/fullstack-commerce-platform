from django.http import JsonResponse
from django.views import View
from django.utils import timezone
from .models import DemoModel


# ---------------------------
# CREATE ONE
# ---------------------------
class CreateOneView(View):
    def post(self, request):
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

        return JsonResponse({"id": obj.id, "message": "created"})


# ---------------------------
# CREATE MANY
# ---------------------------
class CreateManyView(View):
    def post(self, request):
        objs = [
            DemoModel(
                char_field=f"Record {i}",
                text_field="Bulk insert",
                integer_field=i,
                positive_integer_field=i + 1,
                float_field=i + 0.5,
                decimal_field=10 + i,
                boolean_field=(i % 2 == 0),
                date_field=timezone.now().date(),
                datetime_field=timezone.now(),
                time_field=timezone.now().time(),
                status="active",
                url_field="https://example.com",
                email_field=f"user{i}@example.com",
                json_field={"index": i},
            )
            for i in range(5)
        ]

        DemoModel.objects.bulk_create(objs)

        return JsonResponse({"message": "5 records created"})


# ---------------------------
# GET ALL
# ---------------------------
class GetAllView(View):
    def get(self, request):
        data = list(DemoModel.objects.values())
        return JsonResponse({"count": len(data), "data": data})


# ---------------------------
# GET ONE
# ---------------------------
class GetOneView(View):
    def get(self, request, id):
        try:
            obj = DemoModel.objects.get(id=id)
            return JsonResponse({
                "id": obj.id,
                "char_field": obj.char_field,
                "integer_field": obj.integer_field,
                "status": obj.status,
                "json_field": obj.json_field,
            })
        except DemoModel.DoesNotExist:
            return JsonResponse({"error": "not found"}, status=404)


# ---------------------------
# UPDATE
# ---------------------------
class UpdateOneView(View):
    def put(self, request, id):
        try:
            obj = DemoModel.objects.get(id=id)

            obj.char_field = "Updated"
            obj.integer_field = 999
            obj.boolean_field = False
            obj.datetime_field = timezone.now()
            obj.save()

            return JsonResponse({"message": "updated"})
        except DemoModel.DoesNotExist:
            return JsonResponse({"error": "not found"}, status=404)


# ---------------------------
# DELETE
# ---------------------------
class DeleteOneView(View):
    def delete(self, request, id):
        deleted, _ = DemoModel.objects.filter(id=id).delete()

        if deleted == 0:
            return JsonResponse({"error": "not found"}, status=404)

        return JsonResponse({"message": "deleted"})