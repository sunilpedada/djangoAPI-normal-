from django.db import models

# Create your models here.
class EmployeesDetails(models.Model):
    ename=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    eaddress=models.TextField(null=False)
    ephone_number=models.IntegerField()
    esalary=models.IntegerField()

