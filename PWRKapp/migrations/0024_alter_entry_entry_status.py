# Generated by Django 5.1.3 on 2024-12-13 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PWRKapp', '0023_alter_entry_entry_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_status',
            field=models.CharField(blank=True, default='Nowy', max_length=30),
        ),
    ]
