# Generated by Django 4.1 on 2022-08-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0009_country_alter_address_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='published_countries',
            field=models.ManyToManyField(related_name='books', to='book_outlet.country'),
        ),
    ]