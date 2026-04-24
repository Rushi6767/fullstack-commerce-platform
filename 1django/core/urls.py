from django.urls import path
from .views import (
    CreateOneView,
    CreateManyView,
    GetAllView,
    GetOneView,
    UpdateOneView,
    DeleteOneView,
)

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
]