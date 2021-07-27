from django.db import models
class booking_table(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=50)
    date=models.CharField(max_length=25)
    time=models.CharField(max_length=25)

    def __str__(self):
        return self.name

class contact_table(models.Model):
    cname=models.CharField(max_length=50)
    cemail=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

    def __str__(self):
        return self.cname


# Create your models here.
