# Generated by Django 4.0.4 on 2022-06-10 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_rename_features_footerinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='footerinfo',
        ),
    ]
