# Generated by Django 2.1 on 2019-09-26 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190926_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='payout_ampunt',
            field=models.CharField(default=0, max_length=100000),
        ),
    ]