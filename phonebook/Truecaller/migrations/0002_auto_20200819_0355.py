# Generated by Django 3.0.8 on 2020-08-18 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Truecaller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Contact_Number',
            field=models.IntegerField(help_text='Contact Number'),
        ),
    ]
