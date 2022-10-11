# Generated by Django 4.0.5 on 2022-10-11 06:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='effectuerdonarge',
            name='description',
            field=models.CharField(default='salut', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='donateuruser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 11, 6, 51, 40, 341844, tzinfo=utc), verbose_name='last_login'),
        ),
    ]
