# Generated by Django 5.1.3 on 2024-12-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PWRKapp', '0009_file_remove_entry_drawings_2d_entry_drawings_2d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='drawings_2d',
        ),
        migrations.AddField(
            model_name='entry',
            name='drawings_2d',
            field=models.FileField(null=True, upload_to='drawings_2d'),
        ),
    ]
