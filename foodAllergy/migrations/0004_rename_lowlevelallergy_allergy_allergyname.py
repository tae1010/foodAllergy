# Generated by Django 3.2.8 on 2021-11-02 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodAllergy', '0003_delete_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allergy',
            old_name='lowLevelAllergy',
            new_name='allergyName',
        ),
    ]
