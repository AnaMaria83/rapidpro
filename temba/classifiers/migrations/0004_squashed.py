# This is a dummy migration which will be implemented in 6.1

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orgs", "0072_squashed"),
        ("classifiers", "0003_squashed"),
    ]

    operations = []
