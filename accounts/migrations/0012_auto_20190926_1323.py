# Generated by Django 2.1 on 2019-09-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190926_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='payout_ampunt',
            field=models.IntegerField(default=0, max_length=100000),
        ),
    ]
