# Generated by Django 4.0.3 on 2022-06-10 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrumenty', '0003_remove_muzyk_opis'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Instrument',
            new_name='Instruments',
        ),
        migrations.RenameModel(
            old_name='Muzyk',
            new_name='Muzycy',
        ),
        migrations.RenameModel(
            old_name='Rodzaj',
            new_name='Rodzaje',
        ),
    ]