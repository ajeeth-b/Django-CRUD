from django.db import models

# Create your models here.
class Data(models.Model):
    usr_name   = models.CharField(max_length = 30)
    email  = models.EmailField()
    number = models.CharField(max_length = 12)
