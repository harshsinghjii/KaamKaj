# Generated by Django 3.2.6 on 2021-08-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='intern',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]