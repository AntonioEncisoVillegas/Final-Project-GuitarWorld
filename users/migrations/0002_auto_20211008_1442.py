# Generated by Django 3.2.7 on 2021-10-08 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GuitarComercial',
        ),
        migrations.DeleteModel(
            name='GuitarHandMade',
        ),
    ]
