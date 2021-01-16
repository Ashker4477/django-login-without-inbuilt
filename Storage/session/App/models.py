from django.db import models


# Create your models here.
class User(models.Model):
    Profile = models.FileField()
    Name = models.CharField(max_length=100)
    DateOfBirth = models.DateTimeField()
    Email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__ (self):
        return self.Name;
