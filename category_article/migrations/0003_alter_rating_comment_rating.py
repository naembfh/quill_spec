# Generated by Django 4.2.3 on 2023-09-03 14:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_article', '0002_alter_category_options_rating_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_comment',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
