# Generated by Django 5.1.3 on 2024-12-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PWRKapp', '0006_alter_entry_type_of_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='type_of_tool',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='reason',
            field=models.CharField(max_length=100),
        ),
    ]
