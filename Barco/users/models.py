from django.db import models

# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    age = models.IntegerField()
    height = models.DecimalField(max_digits = 3, decimal_places=2)

