# Generated by Django 2.2.4 on 2020-02-27 07:28

from django.db import migrations


def fill_owners(apps, schema_editor):
    flats = apps.get_model('property', 'Flat')
    owners = apps.get_model('property', 'Owner')
    for flat in flats.objects.all():
        flat_owner, created = owners.objects.get_or_create(owner_name=flat.owner_deprecated,
                                                           owner_phone_pure=flat.owner_phone_pure)
        flat_owner.owners_flats.add(flat)



class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20200227_1003'),
    ]

    operations = [
        migrations.RunPython(fill_owners),
    ]
