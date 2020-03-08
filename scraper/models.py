from django.db import models

# Create your models here.


class contactus(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default=None)
    feedback = models.TextField()

    def __str__(self):
        return self.name[:15]