from django.urls import path
from .views import ContactListAPIView

urlpatterns = [
    path(
        "crt/",
        ContactListAPIView.as_view(),
        name="contact-list-api",
    ),
]