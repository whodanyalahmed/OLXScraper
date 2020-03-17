from django.db import models

# Create your models here.


class Contactus(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True,blank=True)
    feedback = models.TextField()

    def __str__(self):
        return self.name[:15]