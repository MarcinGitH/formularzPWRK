# Generated by Django 5.1.3 on 2024-12-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PWRKapp', '0008_employee_entry_comments_entry_drawings_2d_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drawings_2d', models.FileField(null=True, upload_to='drawings_2d')),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='drawings_2d',
        ),
        migrations.AddField(
            model_name='entry',
            name='drawings_2d',
            field=models.ManyToManyField(to='PWRKapp.file'),
        ),
    ]
