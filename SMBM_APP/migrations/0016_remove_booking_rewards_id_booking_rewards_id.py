# Generated by Django 4.2.1 on 2023-05-13 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMBM_APP', '0015_booking_type_slot_type_alter_rewards_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='rewards_id',
        ),
        migrations.AddField(
            model_name='booking',
            name='rewards_id',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='SMBM_APP.rewards'),
        ),
    ]
