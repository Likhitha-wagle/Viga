from django.db import models
import uuid
from department.models import Department
# Create your models here.
class Project(models.Model):
   
    name=models.CharField(max_length=255)
    departments=models.ForeignKey(Department,on_delete=models.CASCADE)

    class Meta:
        db_table = "Project"