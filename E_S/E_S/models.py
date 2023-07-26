from django.db import models


class Profile(models.Model):
    Name = models.CharField(max_length=200)
    Company_Name = models.CharField(max_length=300)
    Designation = models.CharField(max_length=100)
    Location = models.CharField(max_length=1000)
    Phone_Number = models.CharField(max_length=100)

    def __str__(self):
        return self.Name