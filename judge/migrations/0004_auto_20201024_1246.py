# Generated by Django 3.1 on 2020-10-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_auto_20201024_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrun',
            name='time',
            field=models.FloatField(null=True),
        ),
    ]
