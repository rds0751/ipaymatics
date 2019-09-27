from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from accounts.models import Userprofile ,User_account_profile,withdrawal
from django.db.models import Count
from django.db.models.functions import ExtractYear
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from .views import *


@login_required
def home(request):
	if request.method == 'POST':
		if 'fname' in request.POST:
			rr = Userprofile()
			rr.First_name = request.POST['fname']
			rr.Last_name = request.POST['lname']
			rr.account_type = request.POST['account_type']
			rr.Address1 = request.POST['address1']
			rr.Address2 = request.POST['address2']
			rr.refer = request.POST['referal']
			rr.username = request.POST['user']
			print(rr)
			rr.save()
			return redirect('tree')
	return render(request, "home.html", {})

@login_required
def tree_view(request):
    data = Userprofile.objects.all()
    data2 = Userprofile.objects.get(username=request.user)
    w_data = Userprofile.objects.filter(refer=request.user)
    p_data=0
    for kata in w_data:
    	p_data+=kata.no_of_referals
    payout=425*data2.no_of_referals+425*p_data
    wallet=data2.no_of_referals+p_data
    context = {'data': data, 'data2':data2, 'payout':payout, 'wallet':wallet}
    return render(request, "tree.html" , context)

@staff_member_required
@login_required
def admin_dashboard_view(request):
	user_list = Userprofile.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(user_list, 5)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	return render(request, "admindashboard.html",{ 'users': users })

@staff_member_required
@login_required
def admin_dashboard_view_single(request,myid):
    data=Userprofile.objects.filter(id=myid)
    data2=Userprofile.objects.get(id=myid)
    up=data2.username
    withdrawal1 = withdrawal.objects.get(username=up)
    w_data = Userprofile.objects.filter(refer=up)
    p_data=0
    for data in w_data:
    	p_data+=data.no_of_referals
    payout=425*data2.no_of_referals+425*p_data
    if request.method == 'POST':
        if 'payout_cleared' in request.POST:
        	clear = request.POST['payout_cleared']
        	clear2=int(clear)
        	if clear2 <= payout-data2.payout_ampunt :
        		data2.payout_ampunt+=clear2
        		data2.save()
        else:
            print('Errors')
 
    
    data = {'data': data2,'payout':payout, 'withdrawal':withdrawal1}
    return render(request,'admin-single.html',data)


def index(request):
	return render(request, 'base.html')

@login_required
def profile_view(request):
	data=Userprofile.objects.get(username=request.user)
	context={'data':data}
	if  request.method == 'POST':
		data2=Userprofile.objects.filter(id=data.id)
		data2.Profile_pic = request.FILES['profile']
		data2.save()
	else:
		print('Errors')

	return render(request, "myprofile.html",context)

def edit_profile_view(request):
	success=False
	context={'success':success}
	if request.method == 'POST':
		if 'Name_of_account_holder' in request.POST:
			up=User_account_profile()
			up.username = request.user
			up.bank_ifsc = request.POST['bank_ifsc']
			up.Name_of_account_holder = request.POST['Name_of_account_holder']
			up.upi = request.POST['upi']
			up.save()
			success=True
			context={

			'success':success
			}
		else:
			print('Errors')
	return render(request, "edit.html",context)

def withdrwal(request):
	success=False
	context={'success':success}
	if request.method == 'POST':
		if 'withdrawal' in request.POST:
			up=withdrawal()
			up.username = request.user
			up.withdrawal = request.POST['withdrawal']
			up.save()
			success=True
			context={

			'success':success
			}
		else:
			print("Errors")
	return render(request, "withdrwal.html",context)
