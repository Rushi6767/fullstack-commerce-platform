from django.urls import path
from .views import NoteListCreateAPIView, NoteDetailAPIView

urlpatterns = [
    path("notes/", NoteListCreateAPIView.as_view(), name="notes"),
    path("notes/<int:pk>/", NoteDetailAPIView.as_view(), name="note-detail"),
]