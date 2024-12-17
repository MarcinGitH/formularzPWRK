# Generated by Django 5.1.3 on 2024-12-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PWRKapp', '0046_rename_entry_status_entry_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date',
            new_name='change_date',
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
