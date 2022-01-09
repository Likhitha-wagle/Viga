from django.db import models
import uuid
from asset.models import Asset
# Create your models here.
class Department(models.Model):
   
    name=models.CharField(max_length=255)
    assets=models.ForeignKey(Asset,on_delete=models.CASCADE)

    class Meta:
        db_table = "Department"