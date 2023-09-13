# Generated by Django 4.2.3 on 2023-09-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0015_admins_details_admin_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('eventId', models.IntegerField(default=0)),
            ],
        ),
    ]