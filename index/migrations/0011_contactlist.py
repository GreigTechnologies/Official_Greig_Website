# Generated by Django 4.0.4 on 2022-06-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_bg_remove_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField(max_length=1800)),
            ],
        ),
    ]
