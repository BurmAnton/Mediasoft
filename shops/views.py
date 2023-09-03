import random

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics


from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer
from .utils import get_closed_shops, get_opened_shops, add_cities_to_db

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("city"))

class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StreetList(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        streets_cache_name = f'streets_cache_{self.kwargs.get("city_id")}'
        streets_cache = cache.get(streets_cache_name)
        if streets_cache:
            queryset = streets_cache
        else:
            queryset = Street.objects.filter(city=self.kwargs.get('city_id'))
            cache.set(streets_cache_name, queryset, 60 * 60)
        return queryset


class ShopList(APIView):
    def get(self, request, format=None):
        shops = Shop.objects.all()
        
        is_open = self.request.query_params.get('open')
        street = self.request.query_params.get('street')
        city = self.request.query_params.get('city')

        if street is not None and street.isnumeric():
            shops = shops.filter(street=street)
        if city is not None and city.isnumeric():
            shops = shops.filter(city=city)

        if is_open == "1": shops = get_opened_shops(shops)
        elif is_open == "0": shops = get_closed_shops(shops)

        shops = shops.select_related('city', 'street')
        serializer = ShopSerializer(shops, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def generate_shops(request):
    if len(City.objects.all()) < 1000: add_cities_to_db()
    for city_indx, city in enumerate(City.objects.all()):
        for streeet_indx, street in enumerate(city.cities.all()):
            building = random.randint(1, 50)
            opening_time = f'{random.randint(1, 23)}:00'
            closing_time = f'{random.randint(1, 23)}:00'
            shop = Shop.objects.create(
                name=f'Магазин №{city_indx}_{streeet_indx}',
                city=city,
                street=street,
                building=building,
                opening_time=opening_time,
                closing_time=closing_time
            )
            shop.save()
    return HttpResponseRedirect(reverse("admin:shops_shop_changelist"))