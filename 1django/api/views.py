from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from core.models import Contact
from .serializers import ContactSerializer


class ContactListAPIView(APIView):

    def get(self, request):
        contacts = Contact.objects.all()

        serializer = ContactSerializer(
            contacts,
            many=True
        )

        return Response(serializer.data)