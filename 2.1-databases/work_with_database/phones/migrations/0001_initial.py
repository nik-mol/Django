# Generated by Django 4.1.2 on 2022-10-16 07:48

import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=1)),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name', unique=True)),
            ],
        ),
    ]