# Generated by Django 1.9 on 2016-01-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("accounts", "0002_profile_ping_log_limit")]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="token",
            field=models.CharField(blank=True, max_length=128),
        )
    ]
