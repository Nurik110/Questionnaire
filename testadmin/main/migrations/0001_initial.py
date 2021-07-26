# Generated by Django 3.2.5 on 2021-07-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(default='', max_length=8, primary_key=True, serialize=False, verbose_name='Id')),
                ('name', models.CharField(default='', max_length=500, verbose_name='Имя')),
                ('lastame', models.CharField(default='', max_length=500, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
    ]