# Generated by Django 2.1.4 on 2019-01-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("api", "0049_auto_20190102_0743")]

    operations = [
        migrations.AddField(
            model_name="ping",
            name="kind",
            field=models.CharField(blank=True, max_length=6, null=True),
        )
    ]
