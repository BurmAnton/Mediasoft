# Generated by Django 3.2.8 on 2023-09-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0016_auto_20230901_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Название'),
        ),
    ]