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
    HomeView,
    ContactCreateView,
    ContactSuccessView,
    ContactListView,
    ContactUpdateView,
    ContactDeleteView,
    RegisterView,
    LoginView,
    LogoutView
)
from .views import register, user_login, user_logout
from .orm_playground import ORMPlaygroundView


urlpatterns = [
    # CRUD APIs
    path('', HomeView.as_view(), name='home'),
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

    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('success/', ContactSuccessView.as_view(), name='contact_success'),
    path('contacts/', ContactListView.as_view(), name='contact_list'),
    path('update/<int:id>/', ContactUpdateView.as_view(), name='contact_update'),
    path('delete/<int:id>/', ContactDeleteView.as_view(), name='contact_delete'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
