# Generated by Django 3.2.8 on 2021-10-30 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geocoding', '0006_rename_task_link_task_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
