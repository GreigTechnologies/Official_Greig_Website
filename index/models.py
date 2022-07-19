from distutils.command.upload import upload
from email.mime import image
from statistics import mode
from turtle import title
from django.db import models
from django.forms import ImageField

# Create your models here.

class about(models.Model):
    title = models.CharField(max_length=200, blank=False)
    discription = models.TextField(max_length=1800, blank=False)

    def __str__(self):
        return self.title

class slider(models.Model):
    title = models.CharField(max_length=200, blank=False)
    discription = models.TextField(max_length=1800, blank=False)
    

    def __str__(self):
        return self.title

class bg(models.Model):
    image = models.ImageField(upload_to='slider')


class whyus(models.Model):
    image = models.ImageField(upload_to='whyus/')
    title = models.CharField(max_length=200, blank=False)
    discription = models.TextField(max_length=1800, blank=False)

    def __str__(self):
        return self.title

class whyusinfo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    discription = models.TextField(max_length=1800, blank=False)

    def __str__(self):
        return self.title

class service(models.Model):
    title = models.CharField(max_length=100, blank=False)
    discription = models.TextField(max_length=800)

    def __str__(self):
        return self.title

class team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to = 'team/', blank=False)

    def __str__(self):
        return self.name

class partner(models.Model):
    image = models.ImageField(upload_to = 'partner/', blank=False)


class contactlist(models.Model):
    title = models.CharField(max_length=200, blank=False)
    discription = models.TextField(max_length=1800, blank=False)
    
    
class footerinfo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    about = models.TextField(max_length=700, blank=False)


    def __str__(self):
        return self.title


# CONTACT FORM SECTION
class contactform(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=400, blank=False)
    message = models.TextField(max_length=1800, blank=False)

    def __str__(self):
        return self.name