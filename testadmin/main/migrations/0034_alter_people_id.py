# Generated by Django 3.2.5 on 2021-07-23 16:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20210723_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.CharField(default=uuid.UUID('479d73c9-3d1b-4e57-8f1f-ee78a037a471'), editable=False, max_length=500, primary_key=True, serialize=False),
        ),
    ]