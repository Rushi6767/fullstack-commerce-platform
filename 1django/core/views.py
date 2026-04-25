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
    

from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import DemoModel


class PaginatedListView(View):
    def get(self, request):
        page = request.GET.get("page", 1)
        limit = request.GET.get("limit", 5)

        queryset = DemoModel.objects.all().order_by("id")

        paginator = Paginator(queryset, limit)
        page_obj = paginator.get_page(page)

        data = list(page_obj.object_list.values())

        return JsonResponse({
            "page": page_obj.number,
            "total_pages": paginator.num_pages,
            "count": paginator.count,
            "results": data
        })
    

class SearchView(View):
    def get(self, request):
        query = request.GET.get("q", "")

        data = DemoModel.objects.filter(
            char_field__icontains=query
        ).values()

        return JsonResponse({
            "query": query,
            "count": len(data),
            "results": list(data)
        })
    
class OptimizedQueryView(View):
    def get(self, request):

        data = DemoModel.objects.only(
            "id",
            "char_field",
            "email_field"
        ).values()

        return JsonResponse({
            "optimized": True,
            "results": list(data)
        })
    
from django.db.models import Sum, Avg, Max, Min, Count


class AnalyticsView(View):
    def get(self, request):

        stats = DemoModel.objects.aggregate(
            total=Sum("decimal_field"),
            average=Avg("decimal_field"),
            max_value=Max("decimal_field"),
            min_value=Min("decimal_field"),
            count=Count("id"),
        )

        grouped = list(
            DemoModel.objects.values("status")
            .annotate(total=Count("id"))
        )

        return JsonResponse({
            "stats": stats,
            "grouped_by_status": grouped
        })
    

from django.core.cache import cache


class CachedListView(View):
    def get(self, request):

        cached_data = cache.get("demo_list")

        if cached_data:
            return JsonResponse({
                "cached": True,
                "data": cached_data
            })

        data = list(DemoModel.objects.all().values())

        cache.set("demo_list", data, timeout=60)  # 1 min cache

        return JsonResponse({
            "cached": False,
            "data": data
        })