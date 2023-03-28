from django.db import models
from django.db.models.deletion import CASCADE


class City(models.Model):
    name = models.CharField("Название", max_length=100)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField("Название", max_length=100)
    city = models.ForeignKey(
        City, 
        verbose_name="Город", 
        on_delete=CASCADE, 
        related_name='cities',
        blank=False, 
        null=False
    )

    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(
        "Название", 
        max_length=100, 
        blank=False, 
        null=False
    )
    city = models.ForeignKey(
        City, 
        verbose_name="Город", 
        on_delete=CASCADE, 
        related_name='shops',
        blank=False, 
        null=False
    )
    street = models.ForeignKey(
        Street, 
        verbose_name="Улица", 
        on_delete=CASCADE,
        related_name='shops',
        blank=False, 
        null=False
    )
    building = models.CharField(
        "Здание", 
        max_length=10, 
        null=False, 
        blank=False
    )
    opening_time = models.TimeField("Время открытия", null=False, blank=False)
    closing_time = models.TimeField("Время закрытия", null=False, blank=False)

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"

    def __str__(self):
        return self.name