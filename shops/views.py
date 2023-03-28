from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime
from django.db.models import F, Q

from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer


# Create your views here.
class CityList(APIView):
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class StreetList(APIView):
    def get(self, request, city_id, format=None):
        streets = Street.objects.filter(city=city_id)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data)


class ShopList(APIView):
    def get(self, request, format=None):
        shops = Shop.objects.all()
        is_open = self.request.query_params.get('open')
        if is_open in ["0", "1"]:
            current_time = datetime.now().time()
            #shop open
            shops_1 = shops.filter(opening_time__lte=F('closing_time'))
            shops_1 = shops_1.filter(
                opening_time__lte=current_time, 
                closing_time__gte=current_time
            )
            shops_2 = shops.filter(
                Q(opening_time__lte=current_time) | 
                Q(closing_time__gte=current_time),
                opening_time__gt=F('closing_time')
            )
            shops = shops_1 | shops_2
            if is_open == "0":
                #shop close
                shops = Shop.objects.exclude(id__in=shops)
        street = self.request.query_params.get('street')
        if street is not None and street.isnumeric():
            shops = shops.filter(street=street)
        city = self.request.query_params.get('city')
        if city is not None and city.isnumeric():
            shops = shops.filter(city=city)
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)