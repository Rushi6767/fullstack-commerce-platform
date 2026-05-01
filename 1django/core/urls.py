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
from .views import home
from .orm_playground import ORMPlaygroundView


urlpatterns = [
    # CRUD APIs
    path("create/", CreateOneView.as_view()),
    path("create-many/", CreateManyView.as_view()),
    path("all/", GetAllView.as_view()),
    path("get/<int:id>/", GetOneView.as_view()),
    path("update/<int:id>/", UpdateOneView.as_view()),
    path("delete/<int:id>/", DeleteOneView.as_view()),

    # ORM learning playground
    path("orm/", ORMPlaygroundView.as_view()),

    path("page/", PaginatedListView.as_view()),
    path("search/", SearchView.as_view()),
    path("optimized/", OptimizedQueryView.as_view()),
    path("analytics/", AnalyticsView.as_view()),
    path("cached/", CachedListView.as_view()),
    path('', home, name='home'),
]
