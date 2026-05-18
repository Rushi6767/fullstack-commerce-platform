# from django.urls import path
# from .views import NoteListCreateAPIView, NoteDetailAPIView

# urlpatterns = [
#     # path("notes/", NoteListCreateAPIView.as_view(), name="notes"),
#     # path("notes/<int:pk>/", NoteDetailAPIView.as_view(), name="note-detail"),

#     path("notes/", NoteListCreateAPIView.as_view()),
#     path("notes/<int:pk>/", NoteDetailAPIView.as_view()),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NoteViewSet

router = DefaultRouter()
router.register(r"notes", NoteViewSet, basename="note")

urlpatterns = [
    path("", include(router.urls)),
]