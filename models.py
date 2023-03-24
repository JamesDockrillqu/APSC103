from django.db import models
from django.urls import reverse
from django.db import models
from django_google_maps import fields as map_fields


class roadRatings(models.Model):

    # Fields
    RoadSegment = models.CharField(max_length=20, help_text='Coordinates for the Road')
    Rating = models.CharField(max_length=20, help_text='Safety Rating from 1 to 5')


class accountInfo(models.Model):

    # Fields
    username = models.CharField(max_length=20, help_text='Account Username')
    password = models.CharField(max_length=20, help_text='Account Password')


