from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.



class Student(models.Model):

    sem=(
      ('1stsem','1stsem'),
      ('2stsem','2stsem'),
      ('3stsem','3stsem'),
      ('4stsem','4stsem'),
      ('5stsem','5stsem'),
      ('6stsem','6stsem'),



    )
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    year = models.IntegerField(null=True)
    roll_no = models.IntegerField(null=True)
    adress = models.CharField(max_length=500, null=True)
    semester=models.CharField(max_length=200,null=True,choices=sem)
    
    def __str__(self):
        return self.name