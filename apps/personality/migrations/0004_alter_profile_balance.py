# Generated by Django 4.2.5 on 2023-10-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0003_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]