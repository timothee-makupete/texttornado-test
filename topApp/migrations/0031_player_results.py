# Generated by Django 4.2.3 on 2023-09-08 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topApp', '0030_remove_player_amount_of_comments_player_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='results',
            field=models.CharField(default='not seen', max_length=20),
        ),
    ]
