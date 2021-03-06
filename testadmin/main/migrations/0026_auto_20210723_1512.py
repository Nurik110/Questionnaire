# Generated by Django 3.2.5 on 2021-07-23 12:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210723_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='peopleprofile',
            old_name='username',
            new_name='nickname',
        ),
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.CharField(default=uuid.UUID('94b2a63b-2aad-4508-979b-abfb1576aeeb'), editable=False, max_length=500, primary_key=True, serialize=False),
        ),
    ]
