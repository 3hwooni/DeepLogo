# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Images(models.Model):
    trademarkkey = models.BigIntegerField(db_column='TrademarkKey', blank=True, primary_key=True)  # Field name made lowercase.
    viennacode = models.TextField(db_column='viennaCode', blank=True, null=True)  # Field name made lowercase.
    appreferencenumber = models.TextField(db_column='appReferenceNumber', blank=True, null=True)  # Field name made lowercase.
    applicationnumber = models.TextField(db_column='applicationNumber', blank=True, null=True)  # Field name made lowercase.
    sourceimage = models.TextField(db_column='SourceImage', blank=True, null=True)  # Field name made lowercase.
    targetimage = models.TextField(db_column='TargetImage', blank=True, null=True)  # Field name made lowercase.
    rejectdecision = models.TextField(db_column='RejectDecision', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Images'
