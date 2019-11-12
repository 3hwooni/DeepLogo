from django.db import models

# Create your models here.
class Patent(models.Model):
    title = models.CharField(max_length=50)
    imageurl = models.URLField()
    applicationNumber = models.BigIntegerField()
    PublicationNumber = models.BigIntegerField()
    classificationCode = models.BigIntegerField()
    viennaCode = models.BigIntegerField()
    applicantName  = models.CharField(max_length=50)
    publicationNumber = models.BigIntegerField()
    cdate = models.DateTimeField(auto_now=True)
