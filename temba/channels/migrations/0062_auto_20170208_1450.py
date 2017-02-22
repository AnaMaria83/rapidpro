# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0061_channelcount_is_squashed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='channel_type',
            field=models.CharField(choices=[('AT', "Africa's Talking"), ('A', 'Android'), ('BM', 'Blackmyna'), ('CT', 'Clickatell'), ('DA', 'Dart Media'), ('DM', 'Dummy'), ('EX', 'External'), ('FB', 'Facebook'), ('FCM', 'Firebase Cloud Messaging'), ('GL', 'Globe Labs'), ('HX', 'High Connection'), ('H9', 'Hub9'), ('IB', 'Infobip'), ('JS', 'Jasmin'), ('JN', 'Junebug'), ('KN', 'Kannel'), ('LN', 'Line'), ('M3', 'M3 Tech'), ('MB', 'Mblox'), ('NX', 'Nexmo'), ('PL', 'Plivo'), ('SQ', 'Shaqodoon'), ('SC', 'SMSCentral'), ('ST', 'Start Mobile'), ('TG', 'Telegram'), ('T', 'Twilio'), ('TW', 'TwiML Rest API'), ('TMS', 'Twilio Messaging Service'), ('TT', 'Twitter'), ('VB', 'Verboice'), ('VI', 'Viber'), ('VP', 'Viber Public Channels'), ('VM', 'Vumi'), ('VMU', 'Vumi USSD'), ('YO', 'Yo!'), ('ZV', 'Zenvia')], default='A', help_text='Type of this channel, whether Android, Twilio or SMSC', max_length=3, verbose_name='Channel Type'),
        ),
    ]
