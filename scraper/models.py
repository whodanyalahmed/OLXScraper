from django.db import models

# Create your models here.


class contactus(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField()
    email = models.EmailField(max_length=254)
    feedback = models.TextField()

    def __str__(self):
        return self.name[:15]