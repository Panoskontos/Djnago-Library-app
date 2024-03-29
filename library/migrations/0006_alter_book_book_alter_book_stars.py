# Generated by Django 4.0.3 on 2022-03-26 22:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='stars',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.01), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
