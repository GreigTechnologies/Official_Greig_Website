# Generated by Django 4.0.4 on 2022-06-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='bg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slider')),
            ],
        ),
        migrations.RemoveField(
            model_name='slider',
            name='image',
        ),
    ]