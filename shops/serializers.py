from rest_framework import serializers

from .models import City, Street, Shop

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return City.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    

class StreetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    city = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    def create(self, validated_data):
        return Street.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    

class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, 
        allow_blank=False, 
        max_length=100
    )
    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        many=False,
        read_only=False,
        slug_field='name'
    )
    street = serializers.SlugRelatedField(
        queryset=Street.objects.all(),
        many=False,
        read_only=False,
        slug_field='name'
    )
    building = serializers.CharField(
        required=False, 
        allow_blank=True,
        max_length=10
    )
    opening_time = serializers.TimeField(required=False)
    closing_time = serializers.TimeField(required=False)

    def create(self, validated_data):
        return Shop.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.building = validated_data.get('building', instance.building)
        instance.opening_time = validated_data.get(
            'opening_time', 
            instance.opening_time
        )
        instance.closing_time = validated_data.get(
            'closing_time', 
            instance.closing_time
        )
        instance.save()
        return instance