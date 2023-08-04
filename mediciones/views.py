from django.shortcuts import render
from rest_framework import generics

from .models import Area, Region, Measurements
from .serializers import  AreaSerializer, RegionSerializer, MeasurementsSerializer


# Create your views here.
class AreaAPIListView(generics.ListAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()


class AreaAPICreateView(generics.CreateAPIView):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()

class RegionAPIListView(generics.ListAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()

class RegionAPICreateView(generics.CreateAPIView):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class MeasurementsAPIListView(generics.ListAPIView):
    serializer_class = MeasurementsSerializer
    queryset = Measurements.objects.all()

class MeasurementsAPICreateView(generics.CreateAPIView):
    serializer_class = MeasurementsSerializer
    queryset = Measurements.objects.all()

