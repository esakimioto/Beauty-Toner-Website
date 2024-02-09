from django.db import models
from django.db.models import IntegerField, Model

# Create your models here.
class purchase(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    period = models.IntegerField(null=False, default=1)
    prefectures = models.CharField(max_length=128)
    municipalities =models.CharField(max_length=128)
    name1 = models.CharField(max_length=128)
    name2 = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    email_address = models.CharField(max_length=128)
    arrival_date = IntegerField(null=False, default=1)
