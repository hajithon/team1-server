# Generated by Django 5.0.7 on 2024-07-27 10:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("group", "0006_remove_group_user_group_uusers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="group",
            old_name="uusers",
            new_name="users",
        ),
    ]
