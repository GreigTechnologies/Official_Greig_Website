# Generated by Django 4.0.4 on 2022-06-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0010_shipdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipdetail',
            name='discription',
            field=models.TextField(max_length=1000),
        ),
    ]
