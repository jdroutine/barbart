from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    napkinImage = models.ImageField(null=True, blank=True, upload_to="homeImages/")
    gobelinImage = models.ImageField(null=True, blank=True, upload_to="homeImages/")
    tableclothImage = models.ImageField(null=True, blank=True, upload_to="homeImages/")
    coverletImage = models.ImageField(null=True, blank=True, upload_to="homeImages/")
    decorationImage = models.ImageField(null=True, blank=True, upload_to="homeImages/")


    def __str__(self):
        return self.title

class Napkin(models.Model):
    cover = models.ImageField(null=True, blank=True, upload_to="napkinImages/")
    title = models.CharField(null=True, blank=True, max_length=255)
    #content = models.TextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="napkinImages/")
    image1_cover = models.ImageField(null=True, blank=True, upload_to="napkinImages/")
    image2 = models.ImageField(null=True, blank=True, upload_to="napkinImages/")
    image2_cover = models.ImageField(null=True, blank=True, upload_to="napkinImages/")

    def __str__(self):
        return self.title

class Gobelin(models.Model):
    cover = models.ImageField(null=True, blank=True, upload_to="gobelinImages/")
    title = models.CharField(null=True, blank=True, max_length=255)
    #content = models.TextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="gobelinImages/")
    image1_cover = models.ImageField(null=True, blank=True, upload_to="gobelinImages/")
    #image2 = models.ImageField(null=True, blank=True, upload_to="gobelinImages/")
    #image2_cover = models.ImageField(null=True, blank=True, upload_to="gobelinImages/")

    def __str__(self):
        return self.title

class Tablecloth(models.Model):
    cover = models.ImageField(null=True, blank=True, upload_to="tableclothImages/")
    title = models.CharField(null=True, blank=True, max_length=255)
    #content = models.TextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="tableclothImages/")
    image1_cover = models.ImageField(null=True, blank=True, upload_to="tableclothImages/")
    image2 = models.ImageField(null=True, blank=True, upload_to="tableclothImages/")
    image2_cover = models.ImageField(null=True, blank=True, upload_to="tableclothImages/")

    def __str__(self):
        return self.title

class Coverlate(models.Model):
    cover = models.ImageField(null=True, blank=True, upload_to="coverlateImages/")
    title = models.CharField(null=True, blank=True, max_length=255)
    #content = models.TextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="coverlateImages/")
    image1_cover = models.ImageField(null=True, blank=True, upload_to="coverlateImages/")
    image2 = models.ImageField(null=True, blank=True, upload_to="coverlateImages/")
    image2_cover = models.ImageField(null=True, blank=True, upload_to="coverlateImages/")

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Christmas(models.Model):
    cover = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    title = models.CharField(null=True, blank=True, max_length=255)
    #content = models.TextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    image1_cover = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    #image2 = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    #image2_cover = models.ImageField(null=True, blank=True, upload_to="decorationImages/")

    def __str__(self):
        return self.title

class Easter(models.Model):
    cover = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    title = models.CharField(null=True, blank=True, max_length=255)
    #content = models.TextField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    image1_cover = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    #image2 = models.ImageField(null=True, blank=True, upload_to="decorationImages/")
    #image2_cover = models.ImageField(null=True, blank=True, upload_to="decorationImages/")

    def __str__(self):
        return self.title
