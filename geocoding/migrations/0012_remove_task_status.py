# Generated by Django 3.2.8 on 2021-10-31 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocoding', '0011_auto_20211031_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
