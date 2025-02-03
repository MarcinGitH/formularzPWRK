from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    aplication_access = models.BooleanField(null=True)
    admin_access = models.BooleanField()

    def __str__(self):
        return self.name


class File(models.Model):
    drawings_2d = models.FileField(upload_to="drawings_2d", null=True)


class ProducerSupplier(models.Model):
    producer_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.producer_name


class Entry(models.Model):
    PWRK = models.CharField(max_length=10, blank=True)
    description_1 = models.CharField(max_length=100, null=True)
    status = models.CharField(
        max_length=30, null=False, default="NOWY", blank=True)
    type_of_employee = models.CharField(max_length=100, null=False)
    type_of_tool = models.CharField(max_length=30, null=True, blank=True)
    reason = models.CharField(max_length=100, null=True)
    producer = models.ForeignKey(
        ProducerSupplier, on_delete=models.PROTECT, null=True, related_name="producer_data")
    supplier = models.ForeignKey(
        ProducerSupplier, on_delete=models.PROTECT, null=True, related_name="supplier_data")
    entry_employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, null=True, default=1, related_name="entry_employee_data")
    manage_employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, null=True, blank=True, default=2, related_name="manage_employee_data")
    drawings_2d = models.FileField(
        upload_to="drawings_2d", null=True, max_length=300, blank=True)
    drawings_3d = models.FileField(
        upload_to="drawings_3d", null=True, max_length=300, blank=True)
    screen_catalog = models.FileField(
        upload_to="screen_catalog", null=True, max_length=300, blank=True)
    comments = models.TextField(max_length=1000, null=True, blank=True)
    entry_date = models.DateTimeField(
        auto_now=True, blank=True)
    change_date = models.DateTimeField(
        blank=True, null=True)

    def save(self, *args, **kwargs):
        self.form_type = kwargs.pop('form_type', None)
        if self.type_of_employee != "Technolog" and self.form_type == "new_entry_form":
            self.type_of_tool = None
            self.drawings_2d = None
            self.drawings_3d = None
            self.screen_catalog = None
            self.comments = None
        return super(Entry, self).save(*args, **kwargs)
