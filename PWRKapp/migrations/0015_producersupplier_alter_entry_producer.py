# Generated by Django 5.1.3 on 2024-12-13 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PWRKapp', '0014_alter_entry_drawings_2d_alter_entry_drawings_3d'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProducerSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producer_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='producer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='PWRKapp.producersupplier'),
        ),
    ]
