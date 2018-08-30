# Generated by Django 2.0.8 on 2018-08-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("channels", "0100_deactivate_old_twitters")]

    operations = [
        migrations.AlterField(
            model_name="channelevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("unknown", "Unknown Call Type"),
                    ("mt_call", "Outgoing Call"),
                    ("mt_miss", "Missed Outgoing Call"),
                    ("mo_call", "Incoming Call"),
                    ("mo_miss", "Missed Incoming Call"),
                    ("stop_contact", "Stop Contact"),
                    ("new_conversation", "New Conversation"),
                    ("referral", "Referral"),
                ],
                help_text="The type of event",
                max_length=16,
                verbose_name="Event Type",
            ),
        )
    ]