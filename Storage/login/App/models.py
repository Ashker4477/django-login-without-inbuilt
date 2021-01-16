from django.db import models
import datetime
from django.utils import timezone


# Create your models here.


class reg(models.Model):
    fn = models.CharField(max_length=100)
    ln = models.CharField(max_length=100)
    em = models.CharField(max_length=100)
    Dob = models.DateTimeField()
    img = models.FileField()

    def __str__ (self):
        return (self.fn +"\t" + self.ln )
