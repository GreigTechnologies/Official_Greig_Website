# Generated by Django 4.0.4 on 2022-06-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_herosec'),
    ]

    operations = [
        migrations.CreateModel(
            name='features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('list1', models.CharField(max_length=100)),
                ('list2', models.CharField(max_length=100)),
                ('list3', models.CharField(max_length=100)),
                ('list4', models.CharField(max_length=100)),
                ('list5', models.CharField(max_length=100)),
                ('list6', models.CharField(max_length=100)),
                ('list7', models.CharField(max_length=100)),
                ('list8', models.CharField(max_length=100)),
                ('list9', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='fleetmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='fleetmap/')),
            ],
        ),
    ]
