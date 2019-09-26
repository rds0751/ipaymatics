from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Userprofile(models.Model):
	Profile_pic=models.FileField(upload_to='media',default="")
	productinfo=models.CharField(max_length=100,default="")
	First_name=models.CharField(max_length=100,default="")
	Last_name=models.CharField(max_length=100,default="")
	account_type=models.CharField(max_length=100,default="")
	Address1=models.CharField(max_length=100,default="")
	Address2=models.CharField(max_length=100,default="")
	txnid=models.CharField(max_length=100,default="")
	discount=models.CharField(max_length=100,default="")
	net_amount_debit=models.CharField(max_length=100,default="")
	refer = models.CharField(max_length=100)
	no_of_referals=models.IntegerField(default=0)
	payout_ampunt=models.IntegerField(default=0)
	username= models.CharField(max_length=100 ,unique=True)
	def __str__(self):
 		return self.username
