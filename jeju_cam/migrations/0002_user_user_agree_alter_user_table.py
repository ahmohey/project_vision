# Generated by Django 4.2.2 on 2023-07-03 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeju_cam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_agree',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]