# Generated by Django 3.1 on 2020-10-24 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0002_testcase_memory_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='time_limit',
            field=models.FloatField(default=60, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testrun',
            name='time',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
