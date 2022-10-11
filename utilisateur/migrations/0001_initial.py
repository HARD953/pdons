# Generated by Django 4.0.5 on 2022-10-11 06:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import utilisateur.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EffectuerDonArge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donateur', models.CharField(default='issa', max_length=30)),
                ('typeDons', models.CharField(default='null', max_length=30)),
                ('categorieV', models.CharField(default='null', max_length=30)),
                ('cibleV', models.CharField(default='null', max_length=100)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('montant', models.CharField(default='null', max_length=100)),
                ('provider', models.CharField(default='null', max_length=100)),
                ('typePersonne', models.CharField(default='null', max_length=100)),
                ('provenanced', models.CharField(default='null', max_length=100)),
                ('affecter', models.BooleanField(default=False)),
                ('distribuer', models.BooleanField(default=False)),
                ('amount', models.CharField(max_length=30)),
                ('currency', models.CharField(max_length=30)),
                ('matadata', models.CharField(max_length=30)),
                ('operator_id', models.CharField(max_length=30)),
                ('payement_date', models.CharField(max_length=30)),
                ('payement_method', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EffectuerDonNature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donateur', models.CharField(default='issa', max_length=30)),
                ('typeDons', models.CharField(default='null', max_length=30)),
                ('categorieV', models.CharField(default='null', max_length=30)),
                ('cibleV', models.CharField(default='null', max_length=100)),
                ('categorieObjet', models.CharField(default='null', max_length=100)),
                ('typeObjet', models.CharField(default='null', max_length=30)),
                ('lieu_reception', models.CharField(default='null', max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to=utilisateur.models.EffectuerDonNature.nameFile)),
                ('Etat', models.CharField(default='null', max_length=100)),
                ('typePersonne', models.CharField(default='null', max_length=100)),
                ('provenanced', models.CharField(default='null', max_length=100)),
                ('titre', models.CharField(default='null', max_length=100)),
                ('description', models.TextField(default='null', max_length=100)),
                ('affecter', models.BooleanField(default=False)),
                ('distribuer', models.BooleanField(default=False)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonateurUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('user_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(default='ras', max_length=30)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('numero', models.CharField(max_length=30)),
                ('organisations', models.CharField(default='null', max_length=30)),
                ('email1', models.EmailField(max_length=255)),
                ('adresse', models.CharField(default='null', max_length=30)),
                ('numero1', models.CharField(max_length=30)),
                ('last_login', models.DateTimeField(default=datetime.datetime(2022, 10, 11, 6, 34, 36, 520813, tzinfo=utc), verbose_name='last_login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
