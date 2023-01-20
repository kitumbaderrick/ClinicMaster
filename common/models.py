from django.db import models
from django.utils import timezone
# Create your models here.


class LookupObjects(models.Model):
    objectID = models.IntegerField(primary_key=True)
    objectName = models.CharField(max_length=40)
    objectDes =  models.CharField(max_length=60)
    isReadOnly = models.BooleanField(default=0)
    
    class Meta:
        db_table = "LookupObjects"
        verbose_name = 'Look-up Object'
        verbose_name_plural = 'Look-up Objects'

    def __str__(self):
        return self.objectName


class LookupData(models.Model):
    dataID = models.CharField(max_length=20,  primary_key = True)
    objectID = models.ForeignKey(LookupObjects, on_delete=models.CASCADE)
    dataDes = models.CharField('Data Description', max_length=100)
    isDefault = models.BooleanField(default=0)
    isHidden = models.BooleanField(default=0)
    
    class Meta:
        db_table = "LookupData"
        verbose_name = 'Look-up Data'
        verbose_name_plural = 'Look-up Data'


    def __str__(self):
        return self.dataDes
