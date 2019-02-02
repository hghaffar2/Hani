from django.db import models
from .users import User
class Photo(models.Model):

    picture = models.ImageField(upload_to='photos/')

    user = models.ForeignKey(User,on_delete=models.CASCADE)