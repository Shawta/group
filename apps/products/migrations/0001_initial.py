# Generated by Django 5.0.7 on 2024-07-25 06:37

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('type', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50, verbose_name='Type')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Item Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_category', to='categories.category')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
