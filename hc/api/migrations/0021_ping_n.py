# Generated by Django 1.9 on 2016-01-03 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("api", "0020_check_n_pings")]

    operations = [
        migrations.AddField(
            model_name="ping", name="n", field=models.IntegerField(null=True)
        )
    ]
