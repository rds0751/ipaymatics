from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from accounts.models import Userprofile
from django.db.models import Count
from django.db.models.functions import ExtractYear
from django.core.paginator import Paginator
from django.contrib.auth.models import User
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
    data2 = Userprofile.objects.filter(username=request.user)
    w_data = Userprofile.objects.filter(refer=request.user)
    date_joined=request.user.date_joined
    Last_login=request.user.last_login
    date=Last_login-date_joined
    count_w_data = Userprofile.objects.filter(refer=request.user).count()
    q_data = []
    for p in w_data:
    	q_data += Userprofile.objects.filter(refer=p.username)
    wallet = count_w_data + len(q_data)
    amt = 1000+wallet*1000/2
    context = {'data': data, 'wallet': wallet, 'amt': amt,'data2':data2,'date':date}
    return render(request, "tree.html" , context)

@login_required
def savings_view(request):
    date_joined=request.user.date_joined
    Last_login=request.user.last_login
    date=Last_login-date_joined
    I=(6/365)*date.days*(10)
    context = {'date':date,'I':I}
    return render(request, "savings.html" , context)

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

def admin_dashboard_view_single(request,myid):
    data=Userprofile.objects.filter(id=myid)
    data2=Userprofile.objects.get(id=myid)
    payout=440*data2.no_of_referals
    if request.method == 'POST':
        if 'payout_cleared' in request.POST:
        	clear = request.POST['payout_cleared']
        	clear2=int(clear)
        	if clear2 <= payout-data2.payout_ampunt :
        		data2.payout_ampunt+=clear2
        		data2.save()
        else:
            print('Errors')
 
    
    data = {'data': data[0],'payout':payout}
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
