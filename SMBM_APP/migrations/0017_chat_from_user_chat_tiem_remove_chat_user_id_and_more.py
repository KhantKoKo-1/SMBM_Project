# Generated by Django 4.2 on 2023-05-15 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SMBM_APP', '0016_remove_booking_rewards_id_booking_rewards_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='from_user',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='chat',
            name='tiem',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user_id',
        ),
        migrations.AddField(
            model_name='chat',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
