# Generated by Django 2.1 on 2019-09-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20190927_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account_profile',
            name='pan',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='user_account_profile',
            name='uidai',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='productinfo',
            field=models.IntegerField(default=0),
        ),
    ]