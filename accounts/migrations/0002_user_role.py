# Generated by Django 3.2.6 on 2021-09-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('driver', 'Driver'), ('company', 'Company'), ('user', 'User')], default='user', max_length=25, verbose_name='user role'),
        ),
    ]
