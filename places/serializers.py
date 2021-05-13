# drf
from rest_framework import serializers

from .models import Country, City, Location


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class LocationSerializer(serializers.ModelSerializer):
    #city = CitySerializer()
    #country = CountrySerializer()
    location_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['name', 'image', 'description', 'country', 'city', 'location_image_url']
    
    def get_location_image_url(self, obj):
        return obj.image.url if obj.image else ""
