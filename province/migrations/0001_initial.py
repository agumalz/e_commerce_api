# Generated by Django 5.0.1 on 2024-01-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProvinceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_id', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
            ],
        ),
    ]