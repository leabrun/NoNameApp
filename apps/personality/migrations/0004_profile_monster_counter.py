# Generated by Django 4.2.5 on 2023-10-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personality', '0003_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='monster_counter',
            field=models.JSONField(default={'black_monster': 0, 'blue_monster': 0, 'red_monster': 0, 'yellow_monser': 0}),
        ),
    ]
