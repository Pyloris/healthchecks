# Generated by Django 5.0.1 on 2024-02-06 00:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0101_alter_channel_kind"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="kind",
            field=models.CharField(
                choices=[
                    ("simple", "Simple"),
                    ("cron", "Cron"),
                    ("oncalendar", "OnCalendar"),
                ],
                default="simple",
                max_length=10,
            ),
        ),
    ]
