from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=55)
