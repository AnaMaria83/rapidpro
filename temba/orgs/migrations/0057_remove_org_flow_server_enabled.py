# Generated by Django 2.1.8 on 2019-07-03 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("orgs", "0056_auto_20190703_2011")]

    operations = [migrations.RemoveField(model_name="org", name="flow_server_enabled")]
