from django.urls import path
from .views import (
    CreateOneView,
    CreateManyView,
    GetAllView,
    GetOneView,
    UpdateOneView,
    DeleteOneView,
    PaginatedListView,
    SearchView,
    OptimizedQueryView,
    AnalyticsView,
    CachedListView,
)
from .views import home, contact, contact_success, contact_list, contact_update, contact_delete
from .orm_playground import ORMPlaygroundView


urlpatterns = [
    # CRUD APIs
    path("create/", CreateOneView.as_view()),
    path("create-many/", CreateManyView.as_view()),
    path("all/", GetAllView.as_view()),
    path("get/<int:id>/", GetOneView.as_view()),
    # path("update/<int:id>/", UpdateOneView.as_view()),
    path("delete/<int:id>/", DeleteOneView.as_view()),

    # ORM learning playground
    path("orm/", ORMPlaygroundView.as_view()),

    path("page/", PaginatedListView.as_view()),
    path("search/", SearchView.as_view()),
    path("optimized/", OptimizedQueryView.as_view()),
    path("analytics/", AnalyticsView.as_view()),
    path("cached/", CachedListView.as_view()),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('success/', contact_success, name='contact_success'),


    path('contacts/', contact_list, name='contact_list'),
    path('update/<int:id>/', contact_update, name='contact_update'),
    path('delete/<int:id>/', contact_delete, name='contact_delete'),
]
