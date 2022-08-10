# Generated by Django 4.1 on 2022-08-10 03:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='books',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
