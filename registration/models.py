from django.db import models
from django.conf import settings
from common.models import LookupData
from setup.models import Allergies
from django.utils import timezone

# Create your models here.

 
class Patients(models.Model):
    
    patientno = models.CharField(db_column='PatientNo', primary_key=True, max_length=20)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    genderid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='GenderID', blank=True, null=True)  # Field name made lowercase.
    nationalidno = models.CharField(db_column='NationalIDNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.EmailField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=40, blank=True, null=True)  # Field name made lowercase.
    statusid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='StatusID', blank=True, null=True)  # Field name made lowercase.
  
    tribeid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='TribeID', blank=True, null=True)  # Field name made lowercase.
    countryid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    maritalstatusid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='MaritalStatusID', blank=True, null=True)  # Field name made lowercase.
    careentrypointid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='CareEntryPointID', blank=True, null=True)  # Field name made lowercase.
    religionid = models.ForeignKey(LookupData, models.DO_NOTHING ,  db_column='ReligionID', blank=True, null=True)  # Field name made lowercase.
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Patients', on_delete=models.CASCADE)
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', default=timezone.now)
   
    class Meta:
        db_table = 'Patients'
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'

    def __str__(self):
        return str(self.patientno) + ' - ' + str(self.firstname) + ' ' + str(self.lastname) 



class Appointments(models.Model):
    patientno = models.OneToOneField(Patients, models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    appointmentprecisionid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='AppointmentPrecisionID', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='StartTime', max_length=8, blank=True, null=True)  # Field name made lowercase.
    duration = models.SmallIntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='DoctorSpecialtyID', blank=True, null=True)  # Field name made lowercase.
    appointmentdes = models.CharField(db_column='AppointmentDes', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appointmentstatusid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='AppointmentStatusID', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='Appointments', on_delete=models.CASCADE)
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', default=timezone.now) # Field name made lowercase.
   
    class Meta:
        db_table = 'Appointments'
        unique_together = (('patientno', 'startdate'),)
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return str(self.startdate) + ' --> ' + str(self.patientno)


class Patientallergies(models.Model):
    patientno = models.OneToOneField('Patients', models.DO_NOTHING, db_column='PatientNo', primary_key=True)  # Field name made lowercase.
    allergyno = models.ForeignKey(Allergies, models.DO_NOTHING, db_column='AllergyNo')  # Field name made lowercase.
    reaction = models.CharField(db_column='Reaction', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'PatientAllergies'
        unique_together = (('patientno', 'allergyno'),)

    def __str__(self):
        return str(self.patientno) + ' - ' + str(self.allergyno) + ' ' + str(self.reaction) 


class Visits(models.Model):
    visitno = models.CharField(db_column='VisitNo', primary_key=True, max_length=20)  # Field name made lowercase.
    patientno = models.ForeignKey(Patients, models.DO_NOTHING, db_column='PatientNo', blank=True, null=True)  # Field name made lowercase.
    visitdate = models.DateTimeField(db_column='VisitDate', blank=True, null=True)  # Field name made lowercase.
    doctorspecialtyid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='DoctorSpecialtyID', blank=True, null=True)  # Field name made lowercase.
    visitcategoryid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='VisitCategoryID', blank=True, null=True)  # Field name made lowercase.
    visitstatusid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='VisitStatusID', blank=True, null=True)  # Field name made lowercase.
    accesscashservices = models.BooleanField(db_column='AccessCashServices', blank=True, null=True)  # Field name made lowercase.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='visits', on_delete=models.CASCADE)
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', default=timezone.now)
    visitspriorityid = models.ForeignKey(LookupData, models.DO_NOTHING, db_column='VisitsPriorityID', blank=True, null=True)  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked', blank=True, null=True)  # Field name made lowercase.
   
    class Meta:
        db_table = 'Visits'