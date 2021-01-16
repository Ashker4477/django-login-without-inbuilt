from django.db import models


# Create your models here.
class Register(models.Model):
    Fullname = models.CharField(max_length=100)
    Profile = models.FileField()

    def __str__ (self):
        return self.Fullname;
