from rest_framework import serializers

from .models import Area, Region, Measurements

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        #fields = ['id','name','owner','']  o si son todos con
        model = Area
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'