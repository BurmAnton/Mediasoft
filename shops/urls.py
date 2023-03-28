from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('city/', views.CityList.as_view(), name='city'),
    path(
        'city/<int:city_id>/street/', 
         views.StreetList.as_view(), 
         name='street'
    ),
    path('shop/', views.ShopList.as_view(), name='shop'),
]

urlpatterns = format_suffix_patterns(urlpatterns)