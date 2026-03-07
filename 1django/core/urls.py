from django.urls import path
from . import views

urlpatterns = [
    path('create-one/', views.create_one),
    path('create-many/', views.create_many),
    path('get-all/', views.get_all),
    path('get-one/<int:id>/', views.get_one),
    path('update/<int:id>/', views.update_one),
    path('delete/<int:id>/', views.delete_one),
    path("orm/", views.orm),
]