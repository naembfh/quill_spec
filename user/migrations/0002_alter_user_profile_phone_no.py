# Generated by Django 4.2.3 on 2023-09-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
