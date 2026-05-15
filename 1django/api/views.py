from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Contact
from .serializers import ContactSerializer


class ContactAPIView(APIView):

    def get(self, request):
        contacts = Contact.objects.all()

        serializer = ContactSerializer(
            contacts,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ContactDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Contact, pk=pk)

    def get(self, request, pk):
        contact = self.get_object(pk)

        serializer = ContactSerializer(contact)

        return Response(serializer.data)

    def put(self, request, pk):
        contact = self.get_object(pk)

        serializer = ContactSerializer(
            contact,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        contact = self.get_object(pk)

        serializer = ContactSerializer(
            contact,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        contact = self.get_object(pk)

        contact.delete()

        return Response(
            {
                "message": "Contact deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT
        )