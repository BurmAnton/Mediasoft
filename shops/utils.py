import json

from datetime import datetime
import random
from django.db.models import F, Q

from .models import City, Shop, Street

def get_opened_shops(shops):
    current_time = datetime.now().time()
    return shops.filter(
        (Q(opening_time__lte=F('closing_time')) &
        Q(opening_time__lte=current_time, closing_time__gte=current_time)) | 
        (Q(opening_time__gt=F('closing_time')) &
        (Q(opening_time__lte=current_time) | Q(closing_time__gte=current_time)))
    )
    
def get_closed_shops(shops):
    current_time = datetime.now().time()
    return shops.filter(
        (Q(opening_time__lte=F('closing_time')) &
        (Q(opening_time__gt=current_time) | Q(closing_time__lt=current_time))) | 
        (Q(opening_time__gt=F('closing_time')) &
        Q(opening_time__gt=current_time, closing_time__lt=current_time))
    )

def generate_streets(cities):
    streets_name = [
        'ул. Дзержинского',
        'Московское ш.',
        'бул. Луначарского',
        'ул. Победы',
        'ул. Авроры',
        'Самарская ул.',
        'просп. Металлургов',
        'просп. Победы',
        'ул. Свободы',
        'ул. Чекистов',
        'Южный пер.',
    ]
    streets = []
    for city in cities:
        for street_name in streets_name:
            streets.append(Street(name=street_name, city=city))
    Street.objects.bulk_create(streets)

def add_cities_to_db():
    with open("russian-cities.json", "r") as read_file:
        cities_data = json.load(read_file)
    cities = []
    for city in cities_data:
        cities.append(City(name=city['name']))
    cities = City.objects.bulk_create(cities)
    generate_streets(cities)





