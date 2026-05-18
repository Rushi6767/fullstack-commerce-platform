
"""
View sets
"""
from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by("-id")
    serializer_class = NoteSerializer



"""
DRF Generic Views (Industry Standard)
"""
# from rest_framework import generics
# from .models import Note
# from .serializers import NoteSerializer

# class NoteListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Note.objects.all().order_by("-id")
#     serializer_class = NoteSerializer

# class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .models import Note
# from .serializers import NoteSerializer


# # LIST + CREATE
# class NoteListCreateAPIView(APIView):

#     def get(self, request):
#         notes = Note.objects.all().order_by("-id")
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = NoteSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # RETRIEVE + UPDATE + DELETE
# class NoteDetailAPIView(APIView):

#     def get_object(self, pk):
#         return get_object_or_404(Note, pk=pk)

#     def get(self, request, pk):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, pk):
#         note = self.get_object(pk)
#         serializer = NoteSerializer(note, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         note = self.get_object(pk)
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)