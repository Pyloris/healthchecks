# Generated by Django 5.1.4 on 2024-12-27 09:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0115_flip_api_flip_owner_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="check",
            name="badge_key",
            field=models.UUIDField(default=uuid.uuid4, null=True, unique=True),
        ),
    ]
