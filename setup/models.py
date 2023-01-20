from django.db import models
from common.models import LookupData

# Create your models here.


class Allergies(models.Model):

    allergyno = models.CharField(
        db_column='AllergyNo', primary_key=True, max_length=20)

    allergyname = models.CharField(
        db_column='AllergyName', unique=True, max_length=60, blank=True, null=True)

    allergycategoryid = models.ForeignKey(
        LookupData, models.DO_NOTHING, db_column='AllergyCategoryID', blank=True, null=True)

    class Meta:
        db_table = 'Allergies'
        verbose_name = 'Allergy'
        verbose_name_plural = 'Allergies'

    def __str__(self):
        return self.allergyname
