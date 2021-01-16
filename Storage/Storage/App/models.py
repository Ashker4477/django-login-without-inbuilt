from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class regist(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    Age = models.IntegerField()
    sex = models.CharField(max_length=100)
    DOB = models.DateTimeField('date published')
    em = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    Pincode = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__ (self):
        return [self.fname+self.lname]

    def was_published_recently (self):
        return self.DOB >= timezone.now()-datetime.timedelta(days=1)
