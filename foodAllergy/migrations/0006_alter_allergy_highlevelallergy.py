# Generated by Django 3.2.8 on 2021-11-02 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodAllergy', '0005_alter_allergy_highlevelallergy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergy',
            name='highLevelAllergy',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
