from django.db import models
from django.contrib.auth.models import User


class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class Userprofile(models.Model):
	Profile_pic=models.FileField(upload_to='media',default="")
	productinfo=models.IntegerField(default=0)
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
	username= models.CharField(max_length=100,unique=True)
	def __str__(self):
 		return self.username

class User_account_profile(models.Model):
	username=models.CharField(max_length=100 ,unique=True)
	upi=models.CharField(max_length=100,default="")
	bank_ifsc=models.CharField(max_length=100,default="")
	Name_of_account_holder=models.CharField(max_length=100,default="")
	uidai = models.CharField(max_length=12, default="")
	pan = models.CharField(max_length=12, default="")
	
	def __str__(self):
 		return self.username

class withdrawal(models.Model):
	username=models.CharField(max_length=100 )
	withdrawal=models.CharField(max_length=100 )
	def __str__(self):
 		return self.username
