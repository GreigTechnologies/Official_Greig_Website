from distutils.command.upload import upload
from email.mime import image
from tokenize import blank_re
from turtle import title
from django.db import models

# Create your models here.
# all services hero
class hero(models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.TextField(max_length=2000, blank=False)
    image = models.ImageField(upload_to = 'hero/', blank=False)

    def __str__(self):
        return self.title

class heroabout (models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.TextField(max_length=2000, blank=False)

    def __str__(self):
        return self.title

class about(models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.TextField(max_length=2000, blank=False)
    image = models.ImageField(upload_to = 'about/', blank=False)

    def __str__(self):
        return self.title


# Iridium hero-sec2

class herosec(models.Model):
    title = models.CharField(max_length=100, blank=False)
    list1 = models.CharField(max_length=100, blank=False)
    list2 = models.CharField(max_length=100, blank=False)
    list3 = models.CharField(max_length=100, blank=False)
    list4 = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='herosec2/', blank=False)

    def __str__(self):
        return self.title

# fleet_boradband

class fleetmap(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fleetmap/', blank=False)

    def __str__(self):
        return self.title


class iridummap(models.Model):
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to = 'iridium/', blank=False)


    def __str__(self):
        return self.title


class shipdetail(models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(upload_to = 'iridium/', blank=False)

    def __str__(self):
        return self.title

class client(models.Model):
    image = models.ImageField(upload_to = 'iridium/', blank=False)
