# Generated by Django 4.2 on 2023-05-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMBM_APP', '0004_slot_am_10_slot_am_11_slot_pm_2_slot_pm_3_slot_pm_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='avalible',
            field=models.BooleanField(),
        ),
    ]
