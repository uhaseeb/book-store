# Generated by Django 4.1 on 2022-08-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0004_alter_books_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
