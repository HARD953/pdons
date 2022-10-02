# Generated by Django 4.0.5 on 2022-10-01 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_effectuerdonnature_distribuer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='effectuerdonarge',
            name='distribuer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='donateuruser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 1, 12, 15, 41, 75882, tzinfo=utc), verbose_name='last_login'),
        ),
    ]