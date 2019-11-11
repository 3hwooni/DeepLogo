from django.db import models


class Images(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)
    classification = models.CharField(max_length=200, blank=True, null=True)
    application_num = models.CharField(max_length=200, blank=True, null=True)
    registration_num = models.CharField(max_length=200, blank=True, null=True)
    notice_num = models.CharField(max_length=200, blank=True, null=True)
    vienna_code = models.CharField(max_length=200, blank=True, null=True)
    applicant = models.CharField(max_length=45, blank=True, null=True)
    applicated_date = models.DateField(blank=True, null=True)
    notice_date = models.DateField(blank=True, null=True)
    agent = models.CharField(max_length=45, blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'