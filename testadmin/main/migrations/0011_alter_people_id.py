# Generated by Django 3.2.5 on 2021-07-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_people_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
    ]
