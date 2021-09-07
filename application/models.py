from django.db import models

# Create your models here.
class Moblies(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    features = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=3,max_digits=10)
    reviews = models.TextField()
    descriptions = models.TextField()

    class Meta:
        db_table='Moblies'