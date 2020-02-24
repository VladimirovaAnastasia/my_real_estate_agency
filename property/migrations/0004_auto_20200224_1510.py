# Generated by Django 2.2.4 on 2020-02-24 12:10

from django.db import migrations


def filter_new_buildings(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')

    flats.objects.filter(construction_year__gte=2015).update(new_building=True)
    flats.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(filter_new_buildings),
    ]