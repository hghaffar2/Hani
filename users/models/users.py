from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    GENDER_CHOICES = (('M','Male'),('F','Female'))

    phone = models.CharField( max_length = 12 )

    city = models.CharField( max_length = 10 )

    gender = models.CharField( max_length=1, choices=GENDER_CHOICES )







