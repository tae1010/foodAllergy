# Generated by Django 3.2.8 on 2021-11-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodAllergy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highLevelAllergy', models.CharField(max_length=30)),
                ('lowLevelAllergy', models.CharField(max_length=30)),
                ('level', models.IntegerField()),
                ('myAllergy', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=100)),
                ('productContent', models.TextField()),
                ('allergyResult', models.TextField()),
                ('create_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
