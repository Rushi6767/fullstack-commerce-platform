from django.urls import path
from .views import ContactAPIView, ContactDetailAPIView

urlpatterns = [
    path(
        "crt/",
        ContactAPIView.as_view(),
        name="contact-list-api",
    ),

    path(
        "crt/<int:pk>/",
        ContactDetailAPIView.as_view(),
        name="contact-detail",
    ),
]