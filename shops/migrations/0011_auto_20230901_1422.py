# Generated by Django 3.2.8 on 2023-09-01 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0010_shop_shops_shop_closing_f659ae_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='shop',
            name='shops_shop_closing_f659ae_idx',
        ),
        migrations.AlterField(
            model_name='shop',
            name='closing_time',
            field=models.TimeField(verbose_name='Время закрытия'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='opening_time',
            field=models.TimeField(verbose_name='Время открытия'),
        ),
        migrations.AddIndex(
            model_name='shop',
            index=models.Index(fields=['name', 'city', 'street', 'building', 'closing_time', 'opening_time'], name='shops_shop_name_400cb4_idx'),
        ),
    ]