# Generated by Django 4.1.2 on 2022-10-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='accounts/'),
        ),
    ]