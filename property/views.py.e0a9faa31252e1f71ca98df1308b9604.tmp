from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Property
from .serializers import PropertySerializer
from rest_framework import permissions
# Create your views here.


class PropertyList(ListCreateAPIView):
    # this will do the job of creating/listing our data
    permission_classes = {permissions.IsAuthenticated}
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        serializer.save(property_added_by=self.request.user)

    def get_queryset(self):
        return Property.objects.filter(property_added_by=self.request.user)


class PropertyDetails(RetrieveUpdateDestroyAPIView):
    # this will do the job of creating/listing our data
    serializer_class = PropertySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "property_auto"

    def get_queryset(self):
        return Property.objects.filter(property_added_by=self.request.user)
