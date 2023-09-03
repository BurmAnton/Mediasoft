from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('city/', views.CityList.as_view(), name='city'),
    path(
        'city/<int:city_id>/street/', 
         views.StreetList.as_view(), 
         name='street'
    ),
    path('shop/', views.ShopList.as_view(), name='shop'),
    path('generate/shops', views.generate_shops, name='generate_shops')
]

urlpatterns = format_suffix_patterns(urlpatterns)