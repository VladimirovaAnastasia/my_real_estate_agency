# Generated by Django 2.2.4 on 2020-02-28 16:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_merge_20200227_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_deprecated',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_phone_pure',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='flat',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул:'),
        ),
    ]