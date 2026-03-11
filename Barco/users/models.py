from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(models.Model):
    class UserType(models.IntegerChoices):
        STUDENT = 1
        TEACHER = 2

    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=3, decimal_places=2)
    type = models.IntegerField(choices=UserType)