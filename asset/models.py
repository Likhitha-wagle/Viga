from django.db import models
from django.contrib.contenttypes.fields import GenericRelation


# create your models here
class Asset(models.Model):
    name=models.CharField(max_length=200)

    class Meta:
        db_table = "Asset"