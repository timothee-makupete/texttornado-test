# Generated by Django 4.2.3 on 2023-08-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topApp', '0022_alter_player_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile_pic',
            field=models.ImageField(blank=True, default='user_default_pic_x6puuUx.jpg', null=True, upload_to=''),
        ),
    ]