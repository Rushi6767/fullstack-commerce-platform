from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from django.views import View
from django.views.generic import ListView, UpdateView, TemplateView, FormView, View

from .models import Contact
from .forms import ContactForm, RegisterForm

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm


class HomeView(TemplateView):
    template_name = "home.html"

def is_admin(user):
    return user.is_superuser

class ContactCreateView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_success')

        return render(request, 'contact.html', {'form': form})

class ContactSuccessView(TemplateView):
    template_name = "success.html"

class ContactListView(ListView):
    model = Contact
    template_name = "contact_list.html"
    context_object_name = "contacts"
    ordering = ['-id']


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "contact_update.html"
    success_url = "/contacts/"
    pk_url_kwarg = "id"

@method_decorator([login_required, user_passes_test(is_admin)], name='dispatch')
class ContactDeleteView(View):

    def get(self, request, id):
        contact = get_object_or_404(Contact, id=id)
        return render(request, 'contact_delete.html', {'contact': contact})

    def post(self, request, id):
        contact = get_object_or_404(Contact, id=id)
        contact.delete()
        return redirect('contact_list')

# REGISTER
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # debugging
        return super().form_invalid(form)


# LOGIN
class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/contacts/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


# LOGOUT
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')

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