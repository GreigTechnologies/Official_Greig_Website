# Generated by Django 4.0.4 on 2022-06-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_alter_footerinfo_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner/')),
            ],
        ),
        migrations.DeleteModel(
            name='client',
        ),
    ]
