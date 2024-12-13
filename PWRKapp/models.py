from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    admin_access = models.BooleanField()


class File(models.Model):
    drawings_2d = models.FileField(upload_to="drawings_2d", null=True)


class ProducerSupplier(models.Model):
    producer_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.producer_name


class Entry(models.Model):
    PWRK = models.CharField(max_length=15, blank=True)
    description_1 = models.CharField(max_length=100, null=True)
    entry_status = models.CharField(
        max_length=30, null=False, default="Nowy", blank=True)
    type_of_employee = models.CharField(max_length=100, null=False)
    type_of_tool = models.CharField(max_length=30, null=True)
    reason = models.CharField(max_length=100, null=False)
    producer = models.ForeignKey(
        ProducerSupplier, on_delete=models.PROTECT, null=True, related_name="producer_data")
    supplier = models.ForeignKey(
        ProducerSupplier, on_delete=models.PROTECT, null=True, related_name="supplier_data")
    entry_employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, null=True)
    drawings_2d = models.FileField(
        upload_to="drawings_2d", null=True, max_length=300)
    drawings_3d = models.FileField(
        upload_to="drawings_3d", null=True, max_length=300)
    screen_catalog = models.FileField(
        upload_to="screen_catalog", null=True, max_length=300)
    comments = models.TextField(max_length=300, null=True)
    date = models.DateField(auto_now=True)
