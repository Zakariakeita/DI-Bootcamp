# Generated by Django 4.1.4 on 2022-12-12 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comptes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default=True, upload_to='', verbose_name='Photo de profil'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CREATOR', 'Créateur'), ('SUBSCRIBER', 'Abonné')], default=True, max_length=30, verbose_name='Rôle'),
            preserve_default=False,
        ),
    ]