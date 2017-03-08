from django.db import models
from django_countries.fields import CountryField
from settings import EXPERIENCE_TYPE_CHOICES

class Experience(models.Model):
    user = models.ForeignKey('User')

    experience_type = models.CharField(max_length=4, choices=EXPERIENCE_TYPE_CHOICES)
    experience_name = models.CharField(max_length=200)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_hours = models.FloatField()
    #################################################################################
    #TODO: repeated (yes/no) 2nd start/end date, 3rd start/end date, ... etc
    #################################################################################
    organization_name = models.CharField(max_length=100, blank=True)
    #################################################################################
    #TODO: (state if usa), (province if canada), city dropdown
    #################################################################################
    country = CountryField()
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)

    contact_first_name = models.CharField(max_length=35, blank=True)
    contact_last_name = models.CharField(max_length=35, blank=True)
    contact_title = models.CharFeild(max_length=100, blank=True)
    contact_phone = models.CharField(blank=True)
    contact_email = models.EmailField(blank=True)

    experience_description = models.CharField(max_length=700, blank=True)
    notes = models.TextField(max_length=2000, blank=True)
