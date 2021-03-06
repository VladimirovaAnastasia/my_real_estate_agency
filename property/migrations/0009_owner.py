# Generated by Django 2.2.4 on 2020-02-27 06:52

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20200226_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', unique=True)),
                ('owner_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('owner_phone_pure', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Нормализированный номер владельца')),
                ('owners_phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('owners_flats', models.ManyToManyField(related_name='owns_flats', to='property.Flat', verbose_name='Квартиры в собственности', unique=True)),
            ],
        ),
    ]
