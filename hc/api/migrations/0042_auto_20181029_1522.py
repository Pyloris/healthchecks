# Generated by Django 2.1.2 on 2018-10-29 15:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("api", "0041_check_desc")]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("email", "Email"),
                    ("webhook", "Webhook"),
                    ("hipchat", "HipChat"),
                    ("slack", "Slack"),
                    ("pd", "PagerDuty"),
                    ("pagertree", "PagerTree"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("opsgenie", "OpsGenie"),
                    ("victorops", "VictorOps"),
                    ("discord", "Discord"),
                    ("telegram", "Telegram"),
                    ("sms", "SMS"),
                    ("zendesk", "Zendesk"),
                    ("trello", "Trello"),
                ],
                max_length=20,
            ),
        )
    ]
