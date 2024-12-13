from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    admin_access = models.BooleanField()


class File(models.Model):
    drawings_2d = models.FileField(upload_to="drawings_2d", null=True)


class Entry(models.Model):
    description_1 = models.CharField(max_length=100, null=True)
    type_of_employee = models.CharField(max_length=100, null=False)
    type_of_tool = models.CharField(max_length=30, null=True)
    reason = models.CharField(max_length=100, null=False)
    producer = models.CharField(max_length=100, null=True)
    supplier = models.CharField(max_length=100, null=True)
    entry_employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, null=True)
    drawings_2d = models.FileField(upload_to="drawings_2d", null=True)
    drawings_3d = models.FileField(upload_to="drawings_3d", null=True)
    comments = models.TextField(max_length=300, null=True)
