# Generated by Django 4.2.3 on 2023-08-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topApp', '0021_alter_player_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user_default_pic.png', null=True, upload_to=''),
        ),
    ]